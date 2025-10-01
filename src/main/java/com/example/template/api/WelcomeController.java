package com.example.template.api;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.template.api.dto.WelcomeMessageRequest;
import com.example.template.api.dto.WelcomeMessageResponse;
import com.example.template.service.WelcomeService;

import jakarta.validation.Valid;

@RestController
@RequestMapping("/api/welcome")
public class WelcomeController {

    private final WelcomeService welcomeService;

    public WelcomeController(WelcomeService welcomeService) {
        this.welcomeService = welcomeService;
    }

    @GetMapping
    public ResponseEntity<WelcomeMessageResponse> getWelcomeMessage() {
        String message = welcomeService.getWelcomeMessage();
        return ResponseEntity.ok(new WelcomeMessageResponse(message));
    }

    @PostMapping
    public ResponseEntity<WelcomeMessageResponse> updateWelcomeMessage(
            @RequestBody @Valid WelcomeMessageRequest request) {
        String message = welcomeService.updateWelcomeMessage(request.message());
        return ResponseEntity.ok(new WelcomeMessageResponse(message));
    }
}
