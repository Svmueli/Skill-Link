
# Skill Link

Skill Link is a platform that connects informal workers from emerging economies with remote gig opportunities across various industries. The platform enables users to create profiles, showcase their skills, and apply for job listings, while employers can post jobs and manage applications.

## Features

- **User Registration and Authentication**: Users can register as either a worker or employer and log in to access the platform.
- **Job Posting and Listing**: Employers can post jobs, and workers can view and apply for available job listings.
- **Profile Management**: Workers can create and update profiles to showcase their skills and experiences.
- **Dashboard**: Role-based dashboard providing tailored content for both workers and employers.

## Tech Stack

### Backend
- **Django**: Serves as the backend framework for the platform.
- **Django REST Framework**: Provides a robust API for interacting with the frontend.
- **SQLite**: Database used for local development and testing.

### Frontend
- **Next.js**: React-based framework for building the user interface.
- **Tailwind CSS**: Utility-first CSS framework for styling the frontend components.

## Installation

### Prerequisites
- [Python 3.x](https://www.python.org/)
- [Node.js](https://nodejs.org/) and [npm](https://www.npmjs.com/)
- [Git](https://git-scm.com/)

### Backend Setup

1. Clone the repository:
   ```bash
   git clone git@github.com:<your-username>/Skill-Link.git
   cd Skill-Link
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the backend dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the Django server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd skill-link-frontend
   ```

2. Install the frontend dependencies:
   ```bash
   npm install
   ```

3. Start the Next.js development server:
   ```bash
   npm run dev
   ```

## Usage

- Access the platform by visiting `http://localhost:3000` in your browser.
- Register as either a worker or an employer and explore the features.
- Workers can view job listings, apply for jobs, and manage their profiles.
- Employers can post jobs and review applicants.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push the changes to your branch (`git push origin feature-branch`).
5. Open a pull request to the main branch of the repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


```

