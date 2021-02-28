package it.unisa.c07.biblionet.model.entity;

import it.unisa.c07.biblionet.utils.Length;
import lombok.*;

import javax.persistence.*;

/**
 *  Questa classe rappresenta una domanda del questionario di supporto.
 *  Una domanda un id autogenerato, un testo, e 4 stringhe di risposta.
 *
 *
 */
@Entity
@Data
@AllArgsConstructor
@NoArgsConstructor
@RequiredArgsConstructor
public class Domanda {

    /**
     * Rappresenta l'ID di una domanda.
     */
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private int idDomanda;

    /**
     * Rappresenta il testo della domanda.
     */
    @NonNull
    @Column(nullable = false, length = Length.LENGTH_255)
    private String testoDomanda;

    /**
     * Rappresenta la prima risposta possibile.
     */
    @NonNull
    @Column(nullable = false, length = Length.LENGTH_255)
    private String risposta1;

    /**
     * Rappresenta la seconda risposta possibile.
     */
    @NonNull
    @Column(nullable = false, length = Length.LENGTH_255)
    private String risposta2;

    /**
     * Rappresenta la terza risposta possibile.
     */
    @NonNull
    @Column(nullable = false, length = Length.LENGTH_255)
    private String risposta3;

    /**
     * Rappresenta la quarta risposta possibile.
     */
    @NonNull
    @Column(nullable = false, length = Length.LENGTH_255)
    private String risposta4;
}
