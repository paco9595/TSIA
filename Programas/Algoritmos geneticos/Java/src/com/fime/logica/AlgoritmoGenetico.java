package com.fime.logica;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import com.fime.utilerias.Archivo;
import com.fime.utilerias.Datos;

public class AlgoritmoGenetico {
	
	public void ingresoDeDatos() throws IOException{
		switch (Datos.ingresoDeDatos()) {
		case 1:
			System.out.println("Elegiste ingresar los datos mediante un archivo de tipo CSV");
			List<Integer[]> datos = new ArrayList<>(Archivo.leerCSV());
			if (datos.equals(null)) {
				for (Integer[] integers : datos) {
					System.out.println(Arrays.toString(integers));
				}
			}
			break;
		case 2:
			System.out.println("Elegiste ingresar los datos manualmente");
			break;
		case 3:
			System.out.println("Elegiste ingresar los aleatoriamente");
			break;
		}
	}
}
