package com.fime.utilerias;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

public class Archivo {

	public static List<Integer[]> leerCSV() {
		String file = "C:\\Users\\adrian.briano.garcia\\OneDrive\\FIME\\8° Semestre\\IA\\Repo\\Programas\\Algoritmos geneticos\\Java\\data\\Datos.csv";
		List<Integer[]> datos = new ArrayList<>();
		try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
			String linea = "";
			while ((linea = reader.readLine()) != null) {
				String lineaTemporal[] = linea.split(",");
				Integer[] datosTemporales = new Integer[lineaTemporal.length];
				for (int i = 0; i < datosTemporales.length; i++) {
					if (Datos.ValidarDatos(Integer.parseInt(lineaTemporal[i]))) {
						datosTemporales[i] = Integer.parseInt(lineaTemporal[i]);
					}
				}
				datos.add(datosTemporales);
			}
		}catch (FileNotFoundException e) {
			System.out.println("\nArchivo no encontrado o en formato erroneo favor de verficar que se encuentre en formato CSV");
		}catch (Exception e) {
			System.out.println("\nLos datos ingresados son erroneos, solo se admite 1 y 0");
		}
		return datos;
	}
}
