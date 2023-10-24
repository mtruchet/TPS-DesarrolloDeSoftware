package com.ar.desarrolloSoftware.exception;

public class NotFoundException extends RuntimeException{
    private static final String message = "error";

    public NotFoundException(String message) {
        super(message);
    }
}
