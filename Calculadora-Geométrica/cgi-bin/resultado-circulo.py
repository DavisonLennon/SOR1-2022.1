#!/usr/bin/env python3

import cgi,cgitb
import math
import utils

cgitb.enable()

form = cgi.FieldStorage()

r = float(form.getvalue('raio'))

perimetro = 2 * math.pi * r
area = math.pi * r**2

# Geração da página
print("Content-Type: text/html")
utils.html_header("Resultado Círculo")


html = f"""
<center><h2>Resultado - Círculo</h2></center>
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
                    <td>Raio</td>
                    <td>{r}</td>
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
            </tbody>
        </table>
      </div>"""

print(html)

utils.html_footer()
