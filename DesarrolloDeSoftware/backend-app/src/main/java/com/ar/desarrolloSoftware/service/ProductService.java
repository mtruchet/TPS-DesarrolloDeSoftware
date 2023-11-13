package com.ar.desarrolloSoftware.service;

import com.ar.desarrolloSoftware.dtoFilter.ProductFilterDto;
import com.ar.desarrolloSoftware.exception.NotFoundException;
import com.ar.desarrolloSoftware.models.Product;
import com.ar.desarrolloSoftware.repositories.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
@Service
public class ProductService {

    @Autowired
    private ProductRepository productRepository;

    public Product createProduct(Product product) {
        return productRepository.save(product);
    }

    public Product updateProduct(Long id, Product updatedProduct) {
        Product product = productRepository.findById(id)
                .orElseThrow(() -> new NotFoundException("Product not found with id: " + id));

        product.setName(updatedProduct.getName());
        product.setDescription(updatedProduct.getDescription());
        product.setPrice(updatedProduct.getPrice());
        product.setQuantity(updatedProduct.getQuantity());

        return productRepository.save(product);
    }

    public Product getProductById(Long id) {
        return productRepository.findById(id)
                .orElseThrow(() -> new NotFoundException("Product not found with id: " + id));
    }

    public List<Product> getAllProducts() {
        return productRepository.findAll();
    }

    public void deleteProduct(Long id) {
        productRepository.deleteById(id);
    }

    public List<Product> getAllProductsSortedByPrice() {
        return productRepository.findAllByOrderByPrice();
    }
    public List<Product> getByFilterBusqueda(ProductFilterDto productFilter) {
        String name = productFilter.getName();
        String description = productFilter.getDescription();
        double price = productFilter.getPrice();

        if (name != null && description != null && price > 0) {
            return productRepository.findByNameAndDescriptionAndPrice(name, description, price);
        } else if (name != null && description != null) {
            return productRepository.findByNameAndDescription(name, description);
        } else if (name != null && price > 0) {
            return productRepository.findByNameAndPrice(name, price);
        } else if (description != null && price > 0) {
            return productRepository.findByDescriptionAndPrice(description, price);
        } else if (name != null) {
            return productRepository.findByName(name);
        } else if (description != null) {
            return productRepository.findByDescription(description);
        } else if (price > 0) {
            return productRepository.findByPrice(price);
        } else {
            return productRepository.findAll();
        }
    }


}
