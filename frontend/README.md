
<div style="text-align: center; font-size: 24px; font-weight: bold;">
Rapport du Projet Web  
</div>

<div style="text-align: center; font-size: 18px; margin-top: 10px;">
    <strong>Projet :</strong> Site Web du Club  
    <br/>
    <strong>Membres :</strong>  
    <ul style="list-style: none; padding-left: 0; margin: auto;">
      <li>Elwalid Aboulaakoul</li>
      <li>Serrar Zouhair</li>
      <li>Ben Ahmed Ahmed</li>
    </ul>
    <strong>Encadrant :</strong>Mme. WIJDANE KAISS  
    <br/>
    <strong>Filière / Module :</strong> Dévelopement Digitale 
    <br/>
    <strong>Date de soumission :</strong> [Date]
</div>

<div style="page-break-after: always;"></div>


## Table des matières

1. [Introduction](#introduction)  
2. [Problématique](#problématique)  
3. [Planification et Méthodologie](#planification-et-méthodologie)  
4. [Conception du système](#conception-du-système)  
5. [Implémentation](#implémentation)  
6. [Tests](#tests)  
7. [Résultats et discussion](#résultats-et-discussion)  
8. [Améliorations futures](#améliorations-futures)  
9. [Conclusion](#conclusion)  
10. [Annexes](#annexes)  
11. [Références](#références)

## 🧭 Introduction

Nous avons réalisé un site web pour notre club afin d’assurer sa présence numérique et faciliter la communication avec les membres et le public.

## ❓ Problématique

Le club manquait de visibilité en ligne, ce qui limitait l’accès aux informations et événements. Notre projet répond à cette problématique avec une plateforme simple, moderne et accessible.

## 🛠️ Planification et Méthodologie

### Étapes principales :

1. **Analyse des besoins** :
   - Fonctionnalités attendues :  
     - Formulaire d'inscription pour les nouveaux membres  
     - Réservation de places aux événements  
     - Documentation et traçabilité des activités
   - Contenu des pages : Home, About, Events, Projects, Blog, Contact, Join Us
   - Modélisation des données (Exemple - événements) :
     ```sql
     event_id (PK)
     title
     description
     event_date
     start_time
     end_time
     location (physical/virtual)
     event_link (for virtual events)
     cover_image_url
     registration_required (boolean)
     max_attendees (nullable)
     status (upcoming, ongoing, completed, canceled)
     ```

2. **Développement** (directement après l’analyse) :  
   - Frontend en HTML, SCSS, JS natif  
   - Backend en Python avec FastAPI (en cours, sera connecté via JS)

### Exemple de fonction JS pour générer une carte d'événement :
```js
function createEventCard(event) {
    // Create the main card element
    var eventCard = document.createElement('div');
    eventCard.className = 'event-card';
    // Create image container
    var imageContainer = document.createElement('div');
    imageContainer.className = 'event-card__image-container';
    // Create and append image
    var image = document.createElement('img');
    image.className = 'event-card__image';
    image.src = event.cover_image_url;
    image.alt = event.title;
    imageContainer.appendChild(image);
    // Append image container to card
    eventCard.appendChild(imageContainer);
    // Create content container
    var content = document.createElement('div');
    content.className = 'event-card__content';
    // Create and append title
    var title = document.createElement('h3');
    title.className = 'event-card__title';
    title.textContent = event.title;
    content.appendChild(title);
    // Create meta information section
    var meta = document.createElement('div');
    meta.className = 'event-card__meta';
    // Create and append date
    var date = document.createElement('p');
    date.className = 'event-card__date';
    var calendarIcon = document.createElement('i');
    calendarIcon.className = 'far fa-calendar-alt';
    date.appendChild(calendarIcon);
    date.appendChild(document.createTextNode(' ' + event.event_date));
    meta.appendChild(date);
    // Create and append platform/location
    var platform = document.createElement('p');
    platform.className = 'event-card__platform';
    var locationIcon = document.createElement('i');
    locationIcon.className = 'fas fa-map-marker-alt';
    platform.appendChild(locationIcon);
    // Display either physical location or "Online" for virtual events
    var locationText = event.location === 'virtual' ? 'Online' : event.location;
    platform.appendChild(document.createTextNode(' ' + locationText));
    meta.appendChild(platform);
    // Append meta section to content
    content.appendChild(meta);
    // Create speakers section
    var speakers = document.createElement('p');
    speakers.className = 'event-card__speakers';
    var speakersLabel = document.createElement('strong');
    speakersLabel.textContent = 'Speakers:';
    speakers.appendChild(speakersLabel);
    speakers.appendChild(document.createTextNode(' ' + event.speakers.join(', ')));
    content.appendChild(speakers);
    // Create and append description
    var description = document.createElement('p');
    description.className = 'event-card__description';
    description.textContent = event.description;
    content.appendChild(description);
    // Create and append button
    var button = document.createElement('a');
    button.className = 'btn btn-outline event-card__btn';
    button.href = event.event_link || '#';
    button.textContent = 'Learn More';
    content.appendChild(button);
    // Append content to card
    eventCard.appendChild(content);
    // Add status as a data attribute (can be used for filtering or styling)
    eventCard.setAttribute('data-status', event.status);
    return eventCard;
}
````

## 🧩 Conception du système

### Technologies utilisées :

* **Frontend** : HTML, CSS, SCSS, JavaScript
* **Outils** : GitHub, VS Code

### Pages principales :

* Home
* About
* Events
* Projects
* Blog
* Contact
* Join Us

### Arborescence du projet :

```
.
|-- about.html
|-- blog.html
|-- contact.html
|-- events.html
|-- index.html
|-- css/
|   |-- main.css
|-- js/
|   |-- main.js
|   |-- api-integration.js
|   |-- project-card.js
|   |-- event-card.js
|-- images/
```

## 💻 Implémentation

Chaque membre a développé une partie spécifique du site :

* **Design responsive** via Flexbox et Media Queries
* **Animations et Particules** avec CSS et bibliothèques externes
* **Formulaire de contact** avec validation en JS


## ✅ Résultats et discussion

Site fonctionnel avec plusieurs sections opérationnelles. Le backend est encore en cours d'intégration.

### Difficultés :

* Responsive complexe
* Organisation JS modulaire

## 🚀 Améliorations futures

* Connexion Backend / Frontend avec API
* Ajout d’une interface admin pour gérer le contenu
* Intégration multilingue (FR/AR/EN)

## 🧾 Conclusion

Ce projet nous a permis de :

* Renforcer nos compétences en développement web
* Améliorer notre collaboration
* Documenter toutes les étapes de réalisation

## 📎 Annexes

* Captures d’écran
* Codes sources du projet (HTML, CSS, JS, Python)
