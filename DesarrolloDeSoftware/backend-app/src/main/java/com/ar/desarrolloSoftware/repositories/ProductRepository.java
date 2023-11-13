package com.ar.desarrolloSoftware.repositories;

import com.ar.desarrolloSoftware.models.Product;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
@Repository
public interface ProductRepository extends JpaRepository<Product, Long> {
    List<Product> findAllByOrderByPrice();

    List<Product> findByName(String name);
    List<Product> findByDescription(String description);
    List<Product> findByPrice(Double price);
    List<Product> findByNameAndDescription(String name, String description);
    List<Product> findByNameAndPrice(String name, Double price);
    List<Product> findByDescriptionAndPrice(String description, Double price);
    List<Product> findByNameAndDescriptionAndPrice(String name, String description, Double price);

}
