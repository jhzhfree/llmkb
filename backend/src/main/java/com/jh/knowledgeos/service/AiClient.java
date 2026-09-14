package com.jh.knowledgeos.service;
import org.springframework.beans.factory.annotation.Value;import org.springframework.stereotype.Service;import org.springframework.web.client.RestTemplate;import java.util.*;
@Service public class AiClient{private final RestTemplate rest;@Value("${knowledge.ai-service-base-url}")private String base;public AiClient(RestTemplate r){rest=r;}@SuppressWarnings("unchecked")public Map<String,Object> post(String path,Object body){return rest.postForObject(base+path,body,Map.class);}}
