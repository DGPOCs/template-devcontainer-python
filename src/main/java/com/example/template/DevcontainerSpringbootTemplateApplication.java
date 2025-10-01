package com.example.template;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.properties.EnableConfigurationProperties;

import com.example.template.config.WelcomeProperties;

@SpringBootApplication
@EnableConfigurationProperties(WelcomeProperties.class)
public class DevcontainerSpringbootTemplateApplication {

    public static void main(String[] args) {
        SpringApplication.run(DevcontainerSpringbootTemplateApplication.class, args);
    }
}
