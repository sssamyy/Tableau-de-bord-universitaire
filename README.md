# Tableau de Bord Universitaire – PRAVAN University

## 📌 Présentation

Ce projet est une application web interactive de **gestion et visualisation des données universitaires**, destinée aux administrateurs académiques et responsables pédagogiques.

Elle permet d’afficher, analyser et filtrer les données liées aux :
- **Spécialités**
- **Étudiants**
- **Résultats académiques**

L’application propose des **visualisations dynamiques** à travers plusieurs types de graphiques pour aider à la prise de décision.

---

## 🏗️ Technologies Utilisées

- **Backend** : Flask (Python)
- **Base de données** : MySQL / SQLite (`db_university`)
- **Frontend** : HTML, CSS, JavaScript
- **Visualisation** : Chart.js
- **Communication Client/Serveur** : AJAX

---

## 📊 Visualisations Disponibles

- **Diagramme à barres**  
  Affiche le nombre d’étudiants par année, spécialité ou genre.

- **Graphique linéaire**  
  Montre la comparaison entre les taux de succès et d’échec par spécialité.

- **Camembert (Pie Chart)**  
  Représente la moyenne des moyennes par spécialité.

- **Diagramme en anneau (Doughnut Chart)**  
  Illustre la répartition par genre au sein de chaque spécialité.

- **Bubble Chart**  
  Met en évidence les étudiants ayant des résultats d’excellence (multi-dimensionnel).

---

## 🔁 Fonctionnement de l'AJAX

AJAX permet une communication fluide entre le client et le serveur Flask, sans rechargement de page :
1. La requête est envoyée via `fetch()` ou `XMLHttpRequest`.
2. Flask traite la demande et renvoie une réponse JSON.
3. La page est mise à jour dynamiquement (ex : mise à jour d’un graphique) sans refresh complet.

---
## 📌 Conclusion

Ce tableau de bord permet une exploration intuitive des données académiques avec des visualisations claires et pertinentes. Grâce à Flask et Chart.js, il offre une interface ergonomique, rapide et flexible, adaptée aux besoins des gestionnaires universitaires.
