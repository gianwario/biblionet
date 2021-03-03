package it.unisa.c07.biblionet.preferenzeDiLettura.service;

import it.unisa.c07.biblionet.model.dao.DomandaDAO;
import it.unisa.c07.biblionet.model.dao.GenereDAO;
import it.unisa.c07.biblionet.model.dao.utente.EspertoDAO;
import it.unisa.c07.biblionet.model.dao.utente.LettoreDAO;
import it.unisa.c07.biblionet.model.entity.Domanda;
import it.unisa.c07.biblionet.model.entity.Genere;
import it.unisa.c07.biblionet.model.entity.utente.Esperto;
import it.unisa.c07.biblionet.model.entity.utente.Lettore;
import it.unisa.c07.biblionet.preferenzeDiLettura.service.AIModuleAdapter.PythonAdapter;
import it.unisa.c07.biblionet.preferenzeDiLettura.service.AIModuleAdapter.PythonAdapterImpl;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * @author Alessio Casolaro
 * @author Antonio Della Porta
 */
@Service
@RequiredArgsConstructor
public class PreferenzeDiLetturaServiceImpl implements
                                          PreferenzeDiLetturaService {

    /**
     * Si occupa delle funzioni CRUD per il genere.
     */
    private final GenereDAO genereDAO;

    /**
     * Si occupa delle funzioni CRUD per l'esperto.
     */
    private final EspertoDAO espertoDAO;

    /**
     * Si occupa delle funzioni CRUD per l'utente.
     */
    private final LettoreDAO lettoreDAO;

    /**
     * Si occupa delle funzioni CRUD per la domanda.
     */
    private final DomandaDAO domandaDAO;

    /**
     * Si occupa della chiamata al modulo di IA.
     */
    private final PythonAdapter pythonAdapter = new PythonAdapterImpl();

    /**
     * Implementa la funzionalità di restituire tutti i generi
     * presenti nel database.
     * @return la lista di tutti i generi presenti nel database
     */
    @Override
    public List<Genere> getAllGeneri() {
        return genereDAO.findAll();
    }

    /**
     * Implementa la funzionalità di restituire tutti i generi
     * data una lista di nomi di generi.
     * @param generi i generi da trovare
     * @return la lista di generi contenente solamente i generi effettivamente
     * presenti nel database
     */
    @Override
    public List<Genere> getGeneriByName(final String[] generi) {
        List<Genere> toReturn = new ArrayList<>();

        for (String g: generi) {
            Genere gen = genereDAO.findByName(g);
            if (gen != null) {
                toReturn.add(gen);
            }

        }

        return toReturn;
    }

    /**
     * Implementa la funzionalità di aggiungere una lista di generi
     * ad un esperto.
     * @param generi i generi da inserire
     * @param esperto l'esperto a cui inserirli
     */
    @Override
    public void addGeneriEsperto(final List<Genere> generi,
                                 final Esperto esperto) {
        esperto.setGeneri(generi);
        espertoDAO.save(esperto);
    }

    /**
     * Implementa la funzionalità di aggiungere una lista di generi
     * ad un lettore.
     * @param generi i generi da inserire
     * @param lettore il lettore a cui inserirli
     */
    @Override
    public void addGeneriLettore(final List<Genere> generi,
                                 final Lettore lettore) {
        lettore.setGeneri(generi);
        lettoreDAO.save(lettore);
    }

    /**
     * Implementa la funzionalità di generare 5 domande casuali
     * per un questionario di supporto.
     * @return la lista di domande
     */
    @Override
    public List<Domanda> getDomandeCasuali() {
        List<Domanda> tmp = domandaDAO.findAll();
        Collections.shuffle(tmp);
        List<Domanda> listaDomande = new ArrayList<>();

        for(int i = 0; i < 5; i++)
            listaDomande.add(tmp.get(i));

        return listaDomande;
    }

    /**
     * Implementa la funzionalità di chiamare lo script di Python
     * che effettua le predizioni.
     * @return la lista di domande
     */
    @Override
    public List<String> getRisposte(String r1, String r2, String r3, String r4, String r5) {

        List<String> risposte = pythonAdapter.getAIPrediction(r1, r2, r3, r4, r5);
        return risposte;
    }

}
