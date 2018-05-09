package com.fime.utilerias;

import java.util.Scanner;

public class Datos {

	public static int ingresoDeDatos() {
		int opcion = 0;
		boolean noEsOpcionValida = true;
		do {
			try (Scanner scan = new Scanner(System.in)) {
				System.out.println("Opciones para ingresar los datos:");
				System.out.println("1 .- Archivo CSV");
				System.out.println("2 .- Manualmente");
				System.out.println("3 .- Aleatoriamente");
				System.out.print("Ingrese una opcion valida:");
				try {
					opcion = scan.nextInt();
					if (opcion == 1 || opcion == 2 || opcion == 3) {
						noEsOpcionValida = false;
					}
				} catch (Exception e) {
				}

			} catch (Exception e) {
				// TODO: handle exception
			}

		} while (noEsOpcionValida);
		return opcion;
	}

	public static boolean ValidarDatos(int celda) throws Exception {
		if (celda == 0 || celda == 1) {
			return true;
		} else {

			throw new Exception();
		}
	}
}
