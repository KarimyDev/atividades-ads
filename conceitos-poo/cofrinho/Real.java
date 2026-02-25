package br.com.cofrinho;

/*
 * Real.java — moeda em Reais (BRL)
 *
 * O Real já está em Reais, então converter() retorna o próprio valor.
 */
public class Real extends Moeda {

	public Real(double valor) {
		super(valor);
	}

	@Override
	public void info() {
		// Informação sobre a moeda
		System.out.println("Moedinha: Real — R$ " + String.format("%.2f", valor));
	}

	@Override
	public double converter() {
		// Já está em reais
		return valor;
	}
}