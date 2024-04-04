def FormatacaoReais(reais, format="R$"):
  valor = f"{format}{reais:.2f}".replace(".", ",")
  return valor


def ValorPagamento(desconto_dias_atraso = 0.2):
  while True:
      valor_prestacao = float(input("Qual é o valor da prestação[0 para parar]? ")) 
      if valor_prestacao == 0:
        break
      dias_atraso = int(input("Quantos dias ficou em atraso? ")) 
      valor_para_ser_pago = valor_prestacao + ((desconto_dias_atraso * dias_atraso) * valor_prestacao)
      valor_para_ser_pago_formatado = FormatacaoReais(valor_para_ser_pago)
      print(valor_para_ser_pago_formatado)


ValorPagamento()