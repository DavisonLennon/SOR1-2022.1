#!/usr/bin/env python3

import cgi,cgitb
import math
import utils

cgitb.enable()

form = cgi.FieldStorage()

l = float(form.getvalue('lado'))
n = float(form.getvalue('n_lados'))

perimetro = n * l
p = perimetro / 2

angulo_central = 2 * math.pi / n
theta = angulo_central / 2

apotema = l / (2 * math.tan(theta))
area = p * apotema

Rc = l / (2 * math.sin(theta))

# Geração da página
print("Content-Type: text/html")
utils.html_header("Resultado Polígono Regular")


html = f"""
<center><h2>Resultado - Polígono Regular</h2></center>
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
                    <td>Quantidade de lados</td>
                    <td>{n}</td>
                    <td>-</td>
                </tr>
                <tr>
                    <td>Medida do lado</td>
                    <td>{l}</td>
                    <td>u.c.</td>
                </tr>
                <tr>
                    <td>Perímetro</td>
                    <td>{perimetro}</td>
                    <td>u.c.</td>
                </tr>
                <tr>
                    <td>Apótema</td>
                    <td>{apotema}</td>
                    <td>u.c.</td>
                </tr>
                <tr>
                    <td>Área</td>
                    <td>{area}</td>
                    <td>u.a.</td>
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
