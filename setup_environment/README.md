
## Scenario

You are a Data Engineer intern developing a Data Warehouse system for a movie ratings dashboard platform. The platform collects user-generated reviews and rating scores for a variety of movies from different sources.

## Business requirements

The goal is to aggregate, analyze, and visualize movie rating trends from both internal and external sources, providing valuable insights into audience preferences and movie performance.

### Core Business Goals

1. **Movie Ratings Analysis** – Aggregate average scores and trends over time.
2. **Audience Preferences Insights** – Track most popular genres and directors.
3. **Performance Benchmarks** – Compare movies based on ratings and review volume.
4. **Viewer Behavior Trends** – Understand rating patterns by user demographics.

#### Reports

* Average rating by genre and year.
* Rating distribution per movie.
* Top-rated movies by year.

#### Dashboards

* Top 10 highest-rated movies in the last 30 days.
* Movie rating trend by genre.
* Average score by user location.

#### KPIs

* Total number of ratings submitted.
* Average rating score overall.
* Most rated movie.
* Top 5 genres by average rating.

## Data Warehouse Design

We will set up a server named `MovieDW_Server` and a PostgreSQL database named `movie_ratings_dw`.

### Sources

The data sources for the project are:

* **Internal Platform** – Custom dataset with user reviews.
* **[OMDb API](https://www.omdbapi.com/)** – External source for movie metadata.
* **Own synthetic user source** – Artificially generated review data for enrichment.

#### Internal Movie Review Source

`movie_reviews_data`

| Column Name  | Data Type   | Description               |
| ------------ | ----------- | ------------------------- |
| review\_id   | VARCHAR(50) | Unique review identifier  |
| user\_id     | VARCHAR(20) | Platform user ID          |
| movie\_id    | VARCHAR(20) | Movie unique identifier   |
| rating       | INT         | Rating score (1–10)       |
| review\_text | TEXT        | Optional review text      |
| review\_date | DATE        | Date of review submission |

#### OMDb Source

`omdb_metadata`

| Column Name      | Data Type   | Description             |
| ---------------- | ----------- | ----------------------- |
| movie\_id        | VARCHAR(20) | Movie unique identifier |
| title            | TEXT        | Movie title             |
| year             | INT         | Year of release         |
| genre            | TEXT        | Comma-separated genres  |
| director         | TEXT        | Director name           |
| runtime\_minutes | INT         | Movie duration          |

#### User Demographic Source

`user_data`

| Column Name        | Data Type   | Description                   |
| ------------------ | ----------- | ----------------------------- |
| user\_id           | VARCHAR(20) | Unique user identifier        |
| age                | INT         | Age of the user               |
| gender             | VARCHAR(10) | Gender of the user            |
| country            | VARCHAR(50) | Country of the user           |
| registration\_date | DATE        | Date user joined the platform |

## Tasks Completed in this Phase

| Step                         | Description                         | Status |
| ---------------------------- | ----------------------------------- | ------ |
| 1.6.1 Install Python         | Installed latest Python version     | ✅ Done |
| 1.6.2 Install pgAdmin 4      | Installed pgAdmin for DB management | ✅ Done |
| 1.6.3 Fork GitHub project    | Created project fork                | ✅ Done |
| 1.6.4 Create local DW        | Set up PostgreSQL DB locally        | ✅ Done |
| 1.6.5 Ingest from API        | Connected to OMDb API               | ✅ Done |
| 1.6.6 Ingest from own source | Loaded local synthetic data         | ✅ Done |

## Resources

* [OMDb API Documentation](https://www.omdbapi.com/)
* [PostgreSQL Beginner Guide](https://www.postgresqltutorial.com/)
* [Data Warehouse Concepts by IBM](https://www.ibm.com/topics/data-warehouse)
* [Star Schema Explained](https://en.wikipedia.org/wiki/Star_schema)
* [Kimball Methodology Overview](https://www.kimballgroup.com/)
