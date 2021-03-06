<h1 align="center">
  <img src="assets/imgs/logo.png" alt="Logo do JAM Bot" width="120">
  <br>
 	JAM Bot - Just an Automated Marketplace
  <br>
</h1>

<h4 align="center">Um chatbot que auxilia no processo de venda e compra</h4>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.8-FFDE57?style=for-the-badge&logo=Python"
         alt="Python">
          </a>
  <a href="https://rasa.com/">
    <img src="https://img.shields.io/badge/Rasa-3.X-6870EE?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAAAfCAMAAABgbzvOAAAAAXNSR0IB2cksfwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAbZQTFRFAAAAsJD3mG71gU7yWhfux6/61sX76+L9////5Nn8spP33c/88Or+wqr5/fv/s5X3zLj6xa35t5n44NP8fkry+vj/+vf/fknyXh3vk2f0xa75XBruqof2waj5mW/1mXD1wKf5czrxw6r5Xhzuq4n3qYX2WxnuXhzv2cr79fH+1cT7jV7zv6X5/v3/gk/ye0Xx39L84NT84dX8YCDv3M782Mj71ML7ro33fEfyYB/vt5r4poL2eEHxXRvuZCXvZSbvaCvwXx7vvKD4uJv4dj/xZifvYiLvgU3y6+P9aS3wzbn69/T+fUjybTLwlmv0hFLzWxjun3f1+fb+nHT1xrD5dDzx/v7/7+j9Xh3ur4/3rIv3/f3/7OT9sZH3jmD0bzTwYiPv28z75939on32/fz/3tH8pYD249f8pID27OX9nXb1uZz4tpn4/Pv/oXv26uL96eD9o372h1fzj2H0xKv5cTjxqYb2cDbwqoj28ev+5Nj82838wKb5cjnxZSfvqIX28On9q4j2ZCbv7uf9xKz5iFfzYyTvcTfw2Mn7iVnz2sr7ilvzjF3z7eb9tJb4dT3x7ub97+j9ag9c9QAAAJJ0Uk5TAP//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////kP//kHAv6/KwAAABwElEQVR4nK3V9VfCUBQH8KdMeQYotk4UULG7xW4xsLtnotiJ3V3/se/uIWOgR9n8/jLuLu9ztvvONoRkx8dXRnwIoGBkRPFPgJ+/pPg5ASWWFKULEBDoTBAOFgqVWq1yFiEYhwqtABGgEW4rDIcLRURkVLSziME4VmjF/TfAxmtJEhxAIhQ6PQX0Oi0fAwBJyfAzxegBpKZhnJ6R6QCyYEjZORTIzcvnUwBAYRG0illPoCSvtKycXFoFACbYpoxKJjqKAFXVNXxqAairh1aDkdG4AcbGJrK6ucXU6joDHvh+Bu4AnzZzO7k+EaA2OLat47dd6OyydLM9vRTo6yeJGyDA4JCSJpYCwyPQGvUcYpJ5bNzCDE/0YvEQIyenaKYp8OMQ62Ywnu1gprk5j10QzeAHYJ5bgAdi0cQtteJlqzUN/jW4wq3abKvcVxYwzrKurUNrY5ObFwGyHyaZwNbkn7KtmvtauwP1lvdvpF2djQJ7jhPev9L2Dw7dAfvRX3N8AmtOz8554AJO2b38BBj0QFyargiglfYVub5hCXF7JxlA6P6B5W9fMoDQ4xMrD0Bo5rlKHoBeXt8MsgCE3j/o8ROw8ogdrDZTEwAAAABJRU5ErkJggg=="
         alt="Rasa">
          </a>
    
</p>

## Descri????o
O JAM ?? um chatbot que ajuda comerciantes e compradores com seus an??ncios e pesquisas. Automatiza o processo de vendas desenvolvendo um an??ncio baseado em um question??rio de produto e distribuindo-o nas plataformas onde est?? dispon??vel, deixando o vendedor sem preocupa????es at?? a entrega da mercadoria. Para o cliente, simplifica o processo de busca e sele????o de itens, filtrando com base nas prefer??ncias do usu??rio e determinando a melhor alternativa para eles.

## Funcionalidades

* Cadastra um produto
* Distribui o an??ncio
* Integra o processo de venda e o processo de compra
* Busca um produto
* Filtra os an??ncios
* Responde quest??es sobre o produto

## Como executar

### Requisitos

* Python 3.7 ou 3.8
* Rasa 3.X

#### Python

```
$ sudo apt install python3
```

#### Instalar depend??ncias

```
$ pip3 install -r requirements.txt
```

#### Treinar modelo
```
$ cd src
$ rasa train
```

#### Executar modelo
```
$ rasa shell models/{{modelo}}.tar.gz
```

---
