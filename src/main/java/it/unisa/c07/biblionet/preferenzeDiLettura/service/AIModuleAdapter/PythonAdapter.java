package it.unisa.c07.biblionet.preferenzeDiLettura.service.AIModuleAdapter;

import java.util.List;

/**
 *
 * Rappresenta l'interfaccia dello Adapter usata
 * dalle classi di BiblioNet per la chiamata ad un API di Python
 *
 * @author Viviana Pentangelo
 * @author Gianmario Voria
 */
public interface PythonAdapter {

    List<String> getAIPrediction(String r1, String r2, String r3, String r4, String r5);
}
