#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INSTALL_DIR "C:\\Program Files\\IoLang"

int is_admin(void)
{
    BOOL admin = FALSE;
    PSID admin_group = NULL;

    SID_IDENTIFIER_AUTHORITY nt_authority = SECURITY_NT_AUTHORITY;

    if (AllocateAndInitializeSid(
            &nt_authority,
            2,
            SECURITY_BUILTIN_DOMAIN_RID,
            DOMAIN_ALIAS_RID_ADMINS,
            0, 0, 0, 0, 0, 0,
            &admin_group))
    {
        CheckTokenMembership(NULL, admin_group, &admin);
        FreeSid(admin_group);
    }

    return admin;
}

int add_to_path(void)
{
    HKEY key;
    LONG result;

    result = RegOpenKeyExA(
        HKEY_LOCAL_MACHINE,
        "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment",
        0,
        KEY_READ | KEY_WRITE,
        &key);

    if (result != ERROR_SUCCESS)
    {
        return 0;
    }

    DWORD type = REG_EXPAND_SZ;
    DWORD size = 0;

    result = RegQueryValueExA(
        key,
        "Path",
        NULL,
        &type,
        NULL,
        &size);

    if (result != ERROR_SUCCESS || size == 0)
    {
        RegCloseKey(key);
        return 0;
    }

    char *path = malloc(size + strlen(";" INSTALL_DIR) + 1);

    if (!path)
    {
        RegCloseKey(key);
        return 0;
    }

    result = RegQueryValueExA(
        key,
        "Path",
        NULL,
        &type,
        (LPBYTE)path,
        &size);

    if (result != ERROR_SUCCESS)
    {
        free(path);
        RegCloseKey(key);
        return 0;
    }

    path[size] = '\0';

    if (strstr(path, INSTALL_DIR) == NULL)
    {
        strcat(path, ";" INSTALL_DIR);

        result = RegSetValueExA(
            key,
            "Path",
            0,
            REG_EXPAND_SZ,
            (const BYTE *)path,
            (DWORD)(strlen(path) + 1));
    }

    free(path);
    RegCloseKey(key);

    if (result != ERROR_SUCCESS)
    {
        return 0;
    }

    SendMessageTimeoutA(
        HWND_BROADCAST,
        WM_SETTINGCHANGE,
        0,
        (LPARAM) "Environment",
        SMTO_ABORTIFHUNG,
        5000,
        NULL);

    return 1;
}

int main(void)
{
    char exe_path[MAX_PATH];
    char source[MAX_PATH];
    char destination[MAX_PATH];

    const char *files[] = {
        "iol.exe",
        "ior.exe",
        "iolang_delete.exe"};

    printf("=====================================\n");
    printf("          IoLang(TM) Setup\n");
    printf("=====================================\n\n");

    printf("[1/4] Checking administrator privileges...\n");

    if (!is_admin())
    {
        printf("ERROR: Administrator privileges are required.\n");
        printf("Please right-click setup.exe and select:\n");
        printf("Run as administrator\n\n");
        system("pause");
        return 1;
    }

    printf("      OK\n\n");

    printf("[2/4] Creating installation directory...\n");

    if (!CreateDirectoryA(INSTALL_DIR, NULL))
    {
        DWORD error = GetLastError();

        if (error != ERROR_ALREADY_EXISTS)
        {
            printf("ERROR: Cannot create %s\n", INSTALL_DIR);
            printf("Windows error: %lu\n\n", error);
            system("pause");
            return 1;
        }
    }

    printf("      OK\n\n");

    printf("[3/4] Installing IoLang...\n");

    if (!GetModuleFileNameA(NULL, exe_path, MAX_PATH))
    {
        printf("ERROR: Cannot determine setup location.\n");
        system("pause");
        return 1;
    }

    char *last_slash = strrchr(exe_path, '\\');

    if (!last_slash)
    {
        printf("ERROR: Invalid setup path.\n");
        system("pause");
        return 1;
    }

    *last_slash = '\0';

    for (int i = 0; i < 3; i++)
    {
        snprintf(
            source,
            MAX_PATH,
            "%s\\%s",
            exe_path,
            files[i]);

        snprintf(
            destination,
            MAX_PATH,
            "%s\\%s",
            INSTALL_DIR,
            files[i]);

        if (GetFileAttributesA(source) == INVALID_FILE_ATTRIBUTES)
        {
            printf("ERROR: %s was not found beside setup.exe.\n", files[i]);
            printf("Expected:\n");
            printf("  %s\n\n", source);
            system("pause");
            return 1;
        }

        if (!CopyFileA(source, destination, FALSE))
        {
            printf("ERROR: Cannot copy %s.\n", files[i]);
            printf("Windows error: %lu\n\n", GetLastError());
            system("pause");
            return 1;
        }

        printf("      Installed: %s\n", destination);
    }

    printf("\n");

    printf("[4/4] Updating system PATH...\n");

    if (!add_to_path())
    {
        printf("ERROR: Cannot update PATH.\n\n");
        system("pause");
        return 1;
    }

    printf("      OK\n\n");

    printf("=====================================\n");
    printf("      IoLang(TM) installed!\n");
    printf("=====================================\n\n");

    printf("Installation directory:\n");
    printf("  %s\n\n", INSTALL_DIR);

    printf("Installed programs:\n");
    printf("  iol.exe\n");
    printf("  ior.exe\n");
    printf("  iolang_delete.exe\n\n");

    printf("Open a NEW CMD or PowerShell window and run:\n\n");

    printf("  iol --version\n");
    printf("  ior --version\n\n");

    printf("Setup completed successfully.\n\n");

    system("pause");

    return 0;
}