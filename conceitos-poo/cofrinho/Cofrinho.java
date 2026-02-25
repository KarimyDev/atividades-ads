package br.com.cofrinho;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/*
 * Cofrinho.java — gerencia as moedinhas
 *
 * Esta classe usa um ArrayList<Moeda> para armazenar objetos
 * polimórficos (Real, Dolar, Euro). Aqui fazemos operações:
 *  - guardarMoedinha: adicionar
 *  - tirarMoedinha: remover por valor
 *  - mostrarMoedinhas: listar
 *  - mostrarTotalConvertido: calcular total em Reais
 */
public class Cofrinho {

	// Coleção privada de moedas (encapsulamento)
	private List<Moeda> colecao = new ArrayList<>();

	// -------------------------------------------------------
	// Guarda uma nova moedinha no cofrinho
	// -------------------------------------------------------
	public void guardarMoedinha(Moeda m) {
		colecao.add(m);
		System.out.println("Prontinho — sua moedinha foi guardada com carinho.");
	}

	// -------------------------------------------------------
	// Tira a primeira moedinha encontrada com o valor informado
	// -------------------------------------------------------
	public void tirarMoedinha(double valorParaTirar) {
		Iterator<Moeda> it = colecao.iterator();

		while (it.hasNext()) {
			Moeda m = it.next();
			if (Double.compare(m.pegarValor(), valorParaTirar) == 0) {
				it.remove();
				System.out.println("Tudo certo — removi a moedinha de valor " + String.format("%.2f", valorParaTirar));
				return;
			}
		}

		System.out.println("Não encontrei nenhuma moedinha com esse valor. Tente novamente.");
	}

	// -------------------------------------------------------
	// Mostra todas as moedinhas do cofrinho (com carinho)
	// -------------------------------------------------------
	public void mostrarMoedinhas() {
		if (colecao.isEmpty()) {
			System.out.println("Seu cofrinho está vazio — que tal começar a guardar hoje? :)");
			return;
		}

		System.out.println("--- Moedinhas guardadas ---");
		for (Moeda m : colecao) {
			m.info(); // polimorfismo: cada tipo imprime seu formato
		}
		System.out.println("--------------------------");
	}

	// -------------------------------------------------------
	// Calcula o total convertido para Reais
	// -------------------------------------------------------
	public double mostrarTotalConvertido() {
		double soma = 0.0;
		for (Moeda m : colecao) {
			soma += m.converter();
		}
		return soma;
	}

	// -------------------------------------------------------
	// Retorna quantas moedinhas estão guardadas
	// -------------------------------------------------------
	public int contarMoedas() {
		return colecao.size();
	}

	// -------------------------------------------------------
	// Esvazia o cofrinho (método auxiliar)
	// -------------------------------------------------------
	public void esvaziarCofrinho() {
		colecao.clear();
		System.out.println("Cofrinho esvaziado. Vamos começar de novo com alegria!");
	}
}
