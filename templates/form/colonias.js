function change(alcaldia, colonia){
    alcaldia = document.getElementById(alcaldia);
    colonia = document.getElementById(colonia);
    colonia.value ="";
    colonia.innerHTML = "";
    if(alcaldia.value == "Comuna_1"){
    var optionArray = ["|","Santo Domingo Savio Nº 1|Santo Domingo Savio Nº 1",
                        "Santo Domingo Sabio Nº 2|Santo Domingo Sabio Nº 2",
                        "Popular|Popular",
                        "Granizal|Granizal",
                        "Villa Guadalupe|Villa Guadalupe",
                        "San Pablo|San Pablo",
                        "Aldea Pablo VI|Aldea Pablo VI",
                        "La Esperanza Nº 2|La Esperanza Nº 2",
                        "El Compromiso|El Compromiso",
                        "La Avanzada|La Avanzada",
                        "Carpinelo|Carpinelo"];
    } else if(alcaldia.value == "Comuna_2"){
    var optionArray = ["|","La Isla|La Isla",
                              "El Playón de Los Comuneros|El Playón de Los Comuneros",
                              "Pablo VI|Pablo VI",
                              "La Frontera|La Frontera",
                              "La Francia|La Francia",
                              "Andalucía|Andalucía",
                              "Villa del Socorro|Villa del Socorro",
                              "Villa Niza|Villa Niza",
                              "Moscú Nº 1|Moscú Nº 1",
                              "Santa Cruz|Santa Cruz",
                              "La Rosa|La Rosa"];                              
    } else if(alcaldia.value == "Comuna_3"){
    var optionArray = ["|","La Salle|La Salle",
                              "Las Granjas|Las Granjas",
                              "Campo Valdes Nº 2|Campo Valdes Nº 2",
                              "Santa Inés|Santa Inés",
                              "El Raizal|El Raizal",
                              "El Pomar|El Pomar",
                              "Manrique Central No. 2|Manrique Central No. 2",
                              "Manrique Oriental|Manrique Oriental",
                              "Versalles Nº 1|Versalles Nº 1",
                              "Versalles Nº 2|Versalles Nº 2",
                              "La Cruz|La Cruz",
                              "Oriente|Oriente",
                              "Maria Cano Carambolas|Maria Cano Carambolas",
                              "San José La Cima Nº 1|San José La Cima Nº 1",
                              "San José La Cima Nº 2|San José La Cima Nº 2"];                           
    } else if(alcaldia.value == "Comuna_4"){
    var optionArray = ["|","Berlín|Berlín",
                              "San Isidro|San Isidro",
                              "Palermo|Palermo",
                              "Bermejal Los Álamos|Bermejal Los Álamos",
                              "Moravia|Moravia",
                              "Sevilla|Sevilla",
                              "San Pedro|San Pedro",
                              "Manrique Central Nº 1|Manrique Central Nº 1",
                              "Campo Valdes Nº 1|Campo Valdes Nº 1",
                              "Las Esmeraldas|Las Esmeraldas",
                              "La Piñuela|La Piñuela",
                              "Aranjuez|Aranjuez",
                              "Brasilia|Brasilia",
                              "Miranda|Miranda"];                            
    } else if(alcaldia.value == "Comuna_5"){ 
    var optionArray = ["|","Toscana|Toscana",
                              "Las Brisas|Las Brisas",
                              "Florencia|Florencia",
                              "Tejelo|Tejelo",
                              "Boyacá|Boyacá",
                              "Héctor Abad Gómez|Héctor Abad Gómez",
                              "Belalcazar|Belalcazar",
                              "Girardot|Girardot",
                              "Tricentenario|Tricentenario",
                              "Castilla|Castilla",
                              "Francisco Antonio Zea|Francisco Antonio Zea",
                              "Alfonso López|Alfonso López",
                              "Caribe|Caribe",
                              "El Progreso|El Progreso"];                           
    } else if(alcaldia.value == "Comuna_6"){
    var optionArray = ["|","Santander|Santander",
                              "Doce de Octubre Nº 1|Doce de Octubre Nº 1",
                              "Doce de Octubre Nº 2|Doce de Octubre Nº 2",
                              "Pedregal|Pedregal",
                              "La Esperanza|La Esperanza",
                              "San Martín de Porres|San Martín de Porres",
                              "Kennedy|Kennedy",
                              "Picacho|Picacho",
                              "Picachito|Picachito",
                              "Mirador del Doce|Mirador del Doce",
                              "Progreso Nº 2|Progreso Nº 2",
                              "El Triunfo|El Triunfo"];                          
    } else if(alcaldia.value == "Comuna_7"){
    var optionArray = ["|","Cerro El Volador|Cerro El Volador",
                              "San Germán|San Germán",
                              "Facultad de Minas Universidad Nacional|Facultad de Minas Universidad Nacional",
                              "La Pilarica|La Pilarica",
                              "Bosques de San Pablo|Bosques de San Pablo",
                              "Altamira|Altamira",
                              "Córdoba|Córdoba",
                              "López de Mesa|López de Mesa",
                              "El Diamante|El Diamante",
                              "Aures Nº 1|Aures Nº 1",
                              "Aures Nº 2|Aures Nº 2",
                              "Bello Horizonte|Bello Horizonte",
                              "Villa Flora|Villa Flora",
                              "Palenque|Palenque",
                              "Robledo|Robledo",
                              "Cucaracho|Cucaracho",
                              "Fuente Clara|Fuente Clara",
                              "Santa Margarita|Santa Margarita",
                              "Olaya Herrera|Olaya Herrera",
                              "Pajarito|Pajarito",
                              "Monteclaro|Monteclaro",
                              "Nueva Villa de La Iguaná|Nueva Villa de La Iguaná"];
    } else if(alcaldia.value == "Comuna_8"){
    var optionArray = ["|","Villa Hermosa|Villa Hermosa",
                            "La Mansión|La Mansión",
                            "San Miguel|San Miguel",
                            "La Ladera|La Ladera",
                            "Batallón Girardot|Batallón Girardot",
                            "Llanaditas|Llanaditas",
                            "Los Mangos|Los Mangos",
                            "Enciso|Enciso",
                            "Sucre|Sucre",
                            "El Pinal|El Pinal",
                            "Trece de Noviembre|Trece de Noviembre",
                            "La Libertad|La Libertad",
                            "Villatina|Villatina",
                            "San Antonio|San Antonio",
                            "Las Estancias|Las Estancias",
                            "Villa Turbay|Villa Turbay",
                            "La Sierra|La Sierra",
                            "Villa Lilliam|Villa Lilliam"];
    } else if(alcaldia.value == "Comuna_9"){
    var optionArray = ["|","Juan Pablo II|Juan Pablo II",
                          " Barrios de Jesús| Barrios de Jesús",
                          "Bombona Nº 2|Bombona Nº 2",
                          "Los Cerros El Vergel|Los Cerros El Vergel",
                          "Alejandro Echavarría|Alejandro Echavarría",
                          "Barrio Caicedo|Barrio Caicedo",
                          "Buenos Aires|Buenos Aires",
                          "Miraflores|Miraflores",
                          "Cataluña|Cataluña",
                          "La Milagrosa|La Milagrosa",
                          "Gerona|Gerona",
                          "El SalvadorEl Salvador",
                          "Loreto|Loreto",
                          "Asomadera Nº 1|Asomadera Nº 1",
                          "Asomadera Nº 2|Asomadera Nº 2",
                          "Asomadera Nº 3|Asomadera Nº 3",
                          "Ocho de Marzo|Ocho de Marzo"];
    } else if(alcaldia.value == "Comuna_10"){
    var optionArray = ["|","Prado|Prado",
                          "Jesús Nazareno|Jesús Nazareno",
                          "Estación Villa|Estación Villa",
                          "San Benito|San Benito",
                          "Guayaquil|Guayaquil",
                          "Corazón de Jesús|Corazón de Jesús",
                          "Perpetuo Socorro|Perpetuo Socorro",
                          "Barrio Colón|Barrio Colón",
                          "Las Palmas|Las Palmas",
                          "Bomboná Nº 1|Bomboná Nº 1",
                          "Boston|Boston",
                          "La Candelaria|La Candelaria",
                          "Los Ángeles|Los Ángeles",
                          "San Diego|San Diego"];
    } else if(alcaldia.value == "Comuna_11"){
    var optionArray = ["|","Carlos E. Restrepo|Carlos E. Restrepo"
                        ,"Suramericana|Suramericana",
                        "Naranjal|Naranjal",
                        "San Joaquín|San Joaquín",
                        "Los Conquistadores|Los Conquistadores",
                        "Bolivariana|Bolivariana",
                        "Laureles|Laureles",
                        "Las Acacias|Las Acacias",
                        "La Castellana|La Castellana",
                        "Lorena|Lorena",
                        "El Velódromo|El Velódromo",
                        "Estadio|Estadio",
                        "Los Colores|Los Colores",
                        "Cuarta Brigada|Cuarta Brigada",
                        "Florida Nueva|Florida Nueva"];
    } else if(alcaldia.value == "Comuna_12"){
    var optionArray = ["|","Ferrini|Ferrini"
                        ,"Calasanz|Calasanz",
                        "Los Pinos|Los Pinos",
                        "La América|La América",
                        "La Floresta|La Floresta",
                        "Santa Lucia|Santa Lucia",
                        "El Danubio|El Danubio",
                        "Campo Alegre|Campo Alegre",
                        "Santa Mónica|Santa Mónica",
                        "Barrio Cristóbal|Barrio Cristóbal",
                        "Simón Bolívar|Simón Bolívar",
                        "Santa Teresita|Santa Teresita",
                        "Calasanz Parte Alta|Calasanz Parte Alta",];
    } else if(alcaldia.value == "Comuna_13"){
    var optionArray = ["|","El Pesebre|El Pesebre",
                          "Blanquizal|Blanquizal",
                          "Santa Rosa de Lima|Santa Rosa de Lima",
                          "Los Alcázares|Los Alcázares",
                          "Metropolitano|Metropolitano",
                          "La Pradera|La Pradera",
                          "Juan XIII La Quiebra|Juan XIII La Quiebra",
                          "San Javier Nº 1|San Javier Nº 1",
                          "San Javier Nº 2|San Javier Nº 2",
                          "Veinte de Julio|Veinte de Julio",
                          "Belencito|Belencito",
                          "Betania|Betania",
                          "El Corazón|El Corazón",
                          "Las Independencias|Las Independencias",
                          "Nuevos Conquistadores|Nuevos Conquistadores",
                          "El Salado|El Salado",
                          "Eduardo Santos|Eduardo Santos",
                          "Antonio Nariño|Antonio Nariño",
                          "El Socorro|El Socorro"];
    } else if(alcaldia.value == "Comuna_14"){
    var optionArray = ["|","Barrio Colombia|Barrio Colombia",
                          "Simesa|Simesa",
                          "Villa Carlota|Villa Carlota",
                          "Castropol|Castropol",
                          "Lalinde|Lalinde",
                          "Las Lomas Nº 1|Las Lomas Nº 1",
                          "Las Lomas Nº 2|Las Lomas Nº 2",
                          "Altos del Poblado|Altos del Poblado",
                          "El Tesoro|El Tesoro",
                          "Los Naranjos|Los Naranjos",
                          "Los Balsos Nº 1|Los Balsos Nº 1",
                          "Los Balsos Nº 2|Los Balsos Nº 2",
                          "San Lucas|San Lucas",
                          "El Diamante Nº 2|El Diamante Nº 2",
                          "El Castillo|El Castillo",
                          "Alejandría|Alejandría",
                          "La Florida|La Florida",
                          "El Poblado|El Poblado",
                          "Manila|Manila",
                          "Astorga|Astorga",
                          "Patio Bonito|Patio Bonito",
                          "La Aguacatala|La Aguacatala",
                          "Santa María de Los Ángeles|Santa María de Los Ángeles"];
    } else if(alcaldia.value == "Comuna_15"){
    var optionArray = ["|","Tenche|Tenche",
                          "Trinidad|Trinidad",
                          "Santa Fé,|Santa Fé,",
                          "Parque Juan Pablo II|Parque Juan Pablo II",
                          "Campo Amor|Campo Amor",
                          "Noel|Noel",
                          "Cristo Rey|Cristo Rey",
                          "Guayabal|Guayabal",
                          "La Colina|La Colina",
                          "El Rodeo|El Rodeo"];
    } else if(alcaldia.value == "Comuna_16"){
    var optionArray = ["|","Fátima|Fátima",
                          "Rosales|Rosales",
                          "Belén|Belén",
                          "Granada|Granada",
                          "San Bernardo|San Bernardo",
                          "Las Playas|Las Playas",
                          "Diego Echevarria|Diego Echevarria",
                          "La Mota|La Mota",
                          "La Hondonada|La Hondonada",
                          "El Rincón|El Rincón",
                          "La Loma de Los Bernal|La Loma de Los Bernal",
                          "La Gloria|La Gloria",
                          "Altavista|Altavista",
                          "La Palma|La Palma",
                          "Los Alpes|Los Alpes",
                          "Las Violetas|Las Violetas",
                          "Las Mercedes|Las Mercedes",
                          "Nueva Villa de Aburrá|Nueva Villa de Aburrá",
                          "Miravalle|Miravalle",
                          "El Nogal – Los Almendros|El Nogal – Los Almendros",
                          "Cerro Nutibara|Cerro Nutibara"];                 
    } else if(alcaldia.value == "Comuna_50"){
    var optionArray = ["|","San Sebastián de Palmitas|San Sebastián de Palmitas"];                 
    } else if(alcaldia.value == "Comuna_60"){
    var optionArray = ["|","San CristóbalSan Cristóbal"];                 
    } else if(alcaldia.value == "Comuna_70"){
    var optionArray = ["|","Altavista|Altavista"];                 
    } else if(alcaldia.value == "Comuna_80"){
    var optionArray = ["|","San Antonio de Prado|San Antonio de Prado"];                 
    } else if(alcaldia.value == "Comuna_90"){
    var optionArray = ["|","Santa Elena|Santa Elena"];                 
};

  for(option = 0;option < optionArray.length; option++){
    var pair = optionArray[option].split("|");
    var newOption = document.createElement("option");
    newOption.value = pair[0];
    newOption.innerHTML = pair[1];
    colonia.options.add(newOption);
  };    
}