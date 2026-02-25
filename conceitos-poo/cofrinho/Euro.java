package br.com.cofrinho;

/*
 * Euro.java — moeda em Euro (EUR)
 *
 * Cotação usada: ajustar manualmente se desejar.
 */
public class Euro extends Moeda {

	// Cotação aproximada
	private static final double COTACAO_EURO = 6.16;

	public Euro(double valor) {
		super(valor);
	}

	@Override
	public void info() {
		System.out.println("Moedinha: Euro — € " + String.format("%.2f", valor)
		+ " (≈ R$ " + String.format("%.2f", converter()) + ")");
	}

	@Override
	public double converter() {
		return valor * COTACAO_EURO;
	}
}