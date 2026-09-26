# test.iol - Demo math library for IoLang

import math
$importpy math_.py
import io

writeconsole "===== IoLang Math Demo ====="
writeconsole ""

writeconsole "Constants:"
writeconsole Pi
writeconsole E
writeconsole Tau
writeconsole Phi
writeconsole ""

writeconsole "Special values:"
writeconsole Nan
writeconsole Infi
writeconsole NInfi
writeconsole ""

writeconsole "Basic arithmetic:"
output "90 + 80 = "
output add(90, 80)
output "\n"

output "500 - 100 = "
output sub(500, 100)
output "\n"

output "12 * 8 = "
output mul(12, 8)
output "\n"

output "100 / 4 = "
output div(100, 4)
output "\n"
output "\n"

writeconsole "Math functions:"
output "sqrt(16) = "
output sqrt(16)
output "\n"

output "abs(-25) = "
output abs(-25)
output "\n"

output "power(2, 10) = "
output power(2, 10)
output "\n"
output "\n"

writeconsole "Trigonometry:"
output "sin(Deg90) = "
output sin(Deg90)
output "\n"

output "cos(0) = "
output cos(0)
output "\n"
output "\n"

writeconsole "===== End of demo ====="