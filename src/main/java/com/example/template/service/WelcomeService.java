package com.example.template.service;

import java.util.concurrent.atomic.AtomicReference;

import org.springframework.stereotype.Service;

import com.example.template.config.WelcomeProperties;

@Service
public class WelcomeService {

    private final AtomicReference<String> welcomeMessage;

    public WelcomeService(WelcomeProperties properties) {
        this.welcomeMessage = new AtomicReference<>(properties.getWelcomeMessage());
    }

    public String getWelcomeMessage() {
        return welcomeMessage.get();
    }

    public String updateWelcomeMessage(String message) {
        welcomeMessage.set(message);
        return welcomeMessage.get();
    }
}
