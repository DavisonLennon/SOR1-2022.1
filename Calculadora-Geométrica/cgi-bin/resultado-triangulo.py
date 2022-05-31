#!/usr/bin/env python3

import cgi,cgitb
import math
import utils

cgitb.enable()

form = cgi.FieldStorage()

a = float(form.getvalue('lado_a'))
b = float(form.getvalue('lado_b'))
c = float(form.getvalue('lado_c'))

perimetro = a + b + c
p = perimetro / 2

area = math.sqrt(p * (p - a) * (p - b) * (p - c))

ha = 2 * area / a
hb = 2 * area / b
hc = 2 * area / c

cosA = (a**2 - b**2 - c**2) / (2 * b * c)
senA = math.sqrt(1 - cosA**2)
Rc = a / (2 * senA)

# Geração da página
print("Content-Type: text/html")
utils.html_header("Resultado Triângulo")


html = f"""
<center><h2>Resultado - Triângulo</h2></center>
    <div class="table-responsive">
        <table class="table table-striped table-sm">
            <thead>
                <tr>
                    <th scope="col">Item</th>
                    <th scope="col">Valor</th>
                    <th scope="col">Unidade</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Lado AB</td>
                    <td>{c}</td>
                    <td>u.c.</td>
                </tr>
                <tr>
                    <td>Lado BC</td>
                    <td>{a}</td>
                    <td>u.c.</td>
                </tr>
                <tr>
                    <td>Lado AC</td>
                    <td>{b}</td>
                    <td>u.c.</td>
                </tr>
                <tr>
                    <td>Perímetro</td>
                    <td>{perimetro}</td>
                    <td>u.c.</td>
                </tr>
                <tr>
                    <td>Área</td>
                    <td>{area}</td>
                    <td>u.a.</td>
                </tr>
                <tr>
                    <td>Altura relativa a AB</td>
                    <td>{hc}</td>
                    <td>u.c.</td>
                </tr>
                <tr>
                    <td>Altura relativa a BC</td>
                    <td>{ha}</td>
                    <td>u.c.</td>
                </tr>
                <tr>
                    <td>Altura relativa a AC</td>
                    <td>{hb}</td>
                    <td>u.c.</td>
                </tr>
                <tr>
                    <td>Raio da circunferência circunscrita</td>
                    <td>{Rc}</td>
                    <td>u.c.</td>
                </tr>
            </tbody>
        </table>
      </div>"""

print(html)


utils.html_footer()
