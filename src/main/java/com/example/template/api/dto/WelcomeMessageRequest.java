package com.example.template.api.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;

public record WelcomeMessageRequest(
        @NotBlank(message = "El mensaje de bienvenida no puede estar vacío.")
        @Size(max = 255, message = "El mensaje de bienvenida no puede superar los 255 caracteres.")
        String message) {
}
