package br.com.cofrinho;

/*
 * Moeda.java — base de todas as moedas
 *
 * Essa classe é abstrata: define o contrato que todas as moedas
 * devem seguir. As classes filhas (Real, Dolar, Euro) implementam
 * info() e converter(), cada uma do seu jeitinho.
 */
public abstract class Moeda {

	// Valor nominal da moeda (por exemplo: 1.0, 0.50)
	protected double valor;

	// Construtor protegido que as subclasses usam para setar o valor
	public Moeda(double valor) {
		this.valor = valor;
	}

	// Cada moeda vai mostrar suas informações de forma amigável
	public abstract void info();

	// Cada moeda sabe converter seu próprio valor para Reais
	public abstract double converter();

	// Retorna o valor (útil para comparações)
	public double pegarValor() {
		return valor;
	}
}