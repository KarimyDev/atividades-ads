package br.com.cofrinho;

/*
 * Dolar.java — moeda em Dólar (USD)
 *
 * Cotação usada: ajustar manualmente se desejar.
 */
public class Dolar extends Moeda {

	// Cotação aproximada
	private static final double COTACAO_DOLAR = 5.34;

	public Dolar(double valor) {
		super(valor);
	}

	@Override
	public void info() {
		System.out.println("Moedinha: Dólar — US$ " + String.format("%.2f", valor)
		+ " (≈ R$ " + String.format("%.2f", converter()) + ")");
	}

	@Override
	public double converter() {
		return valor * COTACAO_DOLAR;
	}
}