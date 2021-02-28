package it.unisa.c07.biblionet.model.dao;

import it.unisa.c07.biblionet.model.entity.Domanda;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Questa classe rappresenta il DAO di una Domanda.
 */
@Repository
public interface DomandaDAO extends JpaRepository<Domanda, Integer> {
}
