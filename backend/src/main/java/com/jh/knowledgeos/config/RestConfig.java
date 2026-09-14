package com.jh.knowledgeos.config;
import org.springframework.context.annotation.*;import org.springframework.web.client.RestTemplate;
@Configuration public class RestConfig{@Bean public RestTemplate restTemplate(){return new RestTemplate();}}
