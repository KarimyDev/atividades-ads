package br.com.cofrinho;

import java.util.InputMismatchException;
import java.util.Scanner;

/*
 *  Principal.java — entrada do programa
 */
public class Principal {

	public static void main(String[] args) {

		Scanner teclado = new Scanner(System.in);
		Cofrinho meuCofrinho = new Cofrinho();
		int opcao = -1;

		// Mensagens iniciais
		System.out.println("\nOlá! Bem-vindo ao Cofrinho da Karimy.");
		System.out.println("Aqui você pode guardar suas moedinhas e ver o total convertido.\n");

		// Loop do menu — permanece até o usuário digitar 0
		while (opcao != 0) {
			exibirMenu();

			try {
				System.out.print("Digite a opção desejada: ");
				opcao = teclado.nextInt();

				switch (opcao) {
				case 1:
					fluxoGuardar(teclado, meuCofrinho);
					break;
				case 2:
					fluxoTirar(teclado, meuCofrinho);
					break;
				case 3:
					meuCofrinho.mostrarMoedinhas();
					System.out.println("Total de moedinhas: " + meuCofrinho.contarMoedas());
					break;
				case 4:
					double total = meuCofrinho.mostrarTotalConvertido();
					System.out.printf("No total, suas moedinhas valem R$ %.2f%n", total);
					break;
				case 5:
					meuCofrinho.esvaziarCofrinho();
					break;
				case 0:
					System.out.println("Obrigada por usar o Cofrinho da Karimy. Até breve!");
					break;
				default:
					System.out.println("Opção inválida — por favor, escolha uma opção do menu.");
				}

			} catch (InputMismatchException ime) {
				// Tratamento de entrada inválida (ex.: texto quando deveria ser número)
				System.out.println("Entrada inválida. Por favor, digite apenas números conforme o menu.");
				teclado.nextLine(); // limpa o buffer do scanner
			}
		}

		teclado.close();
	}

	// Exibe o menu principal com instruções
	private static void exibirMenu() {
		System.out.println("\n===== MENU DO COFRINHO DA KARIMY =====");
		System.out.println("1 - Guardar moedinha");
		System.out.println("2 - Tirar moedinha por valor");
		System.out.println("3 - Listar moedinhas");
		System.out.println("4 - Mostrar total convertido para Reais");
		System.out.println("5 - Esvaziar cofrinho (opcional)");
		System.out.println("0 - Sair");
		System.out.println("======================================");
	}

	// Fluxo para guardar uma moeda: pede tipo e valor e adiciona
	private static void fluxoGuardar(Scanner teclado, Cofrinho cofrinho) {
		System.out.println("\nQual tipo de moedinha você quer guardar?");
		System.out.println("1 - Real (R$)");
		System.out.println("2 - Dólar (US$)");
		System.out.println("3 - Euro (€)");
		System.out.print("Escolha o tipo: ");

		try {
			int tipo = teclado.nextInt();
			System.out.print("Agora informe o valor da moedinha: ");
			double valor = teclado.nextDouble();

			Moeda nova = null;
			if (tipo == 1) {
				nova = new Real(valor);
			} else if (tipo == 2) {
				nova = new Dolar(valor);
			} else if (tipo == 3) {
				nova = new Euro(valor);
			} else {
				System.out.println("Tipo inválido — retornando ao menu.");
				return;
			}

			cofrinho.guardarMoedinha(nova);

		} catch (InputMismatchException e) {
			System.out.println("Entrada inválida. Por favor, informe números válidos.");
			teclado.nextLine(); // limpa buffer
		}
	}

	// Fluxo para tirar uma moeda: pede o valor e tenta remover
	private static void fluxoTirar(Scanner teclado, Cofrinho cofrinho) {
		System.out.print("\nInforme o valor da moedinha que deseja tirar: ");
		try {
			double valor = teclado.nextDouble();
			cofrinho.tirarMoedinha(valor);
		} catch (InputMismatchException e) {
			System.out.println("Entrada inválida. Informe um número válido.");
			teclado.nextLine();
		}
	}
}