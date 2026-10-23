
# Ontologia del perro

## 1. Descripcion

Esta ontologia representas las respuestas que mediante una entreviste obtenida, nos dan la base de la informacion para crear las condiciones,hechos y reglas

## 2. Hechos formalizados

Los hechos se representan mediante predicados asociados al individuo perro.

- `mamifero(perro)`
- `domestico(perro)`
- `ladra(perro)`
- `convive_humanos(perro)`
- `sociable(perro)`
- `amamanta_crias(perro)`
- `crias_vientre_materno(perro)`

## 3. Representación grafica de los hechos

```mermaid
flowchart TD
    P["Perro"]
    P --> M["Mamífero"]
    P --> D["Doméstico"]
    P --> L["Ladra"]
    P --> C["Convive con humanos"]
    P --> S["Sociable"]
    P --> A["Amamanta a sus crías"]
    P --> V["Crías en el vientre materno"]
```

## 4. Reglas de conocimiento

### Regla 1

Si el individuo es mamífero, doméstico y ladra, se concluye que corresponde al concepto perro.

**Formalizacion:**

`perro(X) :- mamifero(X), domestico(X), ladra(X).`

### Regla 2

Si el individuo es mamífero, convive con los seres humanos y es domestico, se concluye que corresponde al concepto perro.

**Formalización:**

`perro(X) :- mamifero(X), convive_humanos(X), domestico(X).`

## 5. Representacion grafica de las reglas

```mermaid
flowchart TD
    M["Es mamífero"] --> R1{"Regla 1"}
    D["Es doméstico"] --> R1
    L["Ladra"] --> R1

    M2["Es mamífero"] --> R2{"Regla 2"}
    C["Convive con humanos"] --> R2
    D2["Es doméstico"] --> R2

    R1 --> P["Conclusión: perro"]
    R2 --> P
```

## 6. Relacion con el programa Python

Los hechos se almacenan mediante tuplas y las reglas se representan mediante tuplas que contienen una conclusión y sus condiciones.

El programa utiliza la funcion `all()` para comprobar si todas las condiciones de cada regla se encuentran en la base de hechos. 

## 7. Conclusion

La ontologia nos permite organizar graficamente el conocimiento obtenido en la entrevista. Los hechos describen las caracteristicas del perro y las reglas permiten evaluar las condiciones para obtener conclusiones mediante Python.
