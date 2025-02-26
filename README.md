<a name="top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br/>
<h3 align="center">Automated Testing with Selenium</h3>

  <p align="center">
    A comprehensive suite of automated tests for web applications using Selenium WebDriver
    <br />
    <a href="https://github.com/HeitorLouzeiroRepositoryIFPI/trabalho-final-eng-testes"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/HeitorLouzeiroRepositoryIFPI/trabalho-final-eng-testes/issues">Report Bug</a>
    ·
    <a href="https://github.com/HeitorLouzeiroRepositoryIFPI/trabalho-final-eng-testes/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#test-cases">Test Cases</a></li>
    <li><a href="#usage">Usage</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#collaborators">Collaborators</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

This project demonstrates automated testing capabilities using Selenium WebDriver, focusing on various web interactions and validations. It includes a comprehensive suite of tests covering different aspects of web application testing, from basic authentication to complex dynamic content handling.

### Built With

* [![Python][Python]][Python-url]
* [![Selenium][Selenium]][Selenium-url]
* [![unittest][unittest]][unittest-url]
* [![Chrome][Chrome]][Chrome-url]

<p align="right">(<a href="#top">back to top</a>)</p>

## Test Cases

### 1. Authentication Tests (CT-Login-001)
- **Purpose**: Verify login functionality
- **Scenarios**:
  - Successful login with valid credentials
  - Failed login with invalid credentials
- **Site**: https://the-internet.herokuapp.com/login

### 2. Form Tests (CT-Form-001)
- **Purpose**: Test form submission and validation
- **Scenarios**:
  - Successful form submission
  - Form validation with missing fields
- **Site**: https://ultimateqa.com/filling-out-forms/

### 3. Alert Tests (CT-Alert-001)
- **Purpose**: Handle JavaScript alerts and prompts
- **Scenarios**:
  - Alert confirmation
  - Prompt interaction with text input
- **Site**: https://the-internet.herokuapp.com/javascript_alerts

### 4. Drag and Drop Tests (CT-Drag-001)
- **Purpose**: Test drag and drop functionality
- **Scenarios**:
  - Element dragging and positioning
  - Position verification
- **Site**: https://the-internet.herokuapp.com/drag_and_drop

### 5. Upload Tests (CT-Upload-001)
- **Purpose**: Verify file upload functionality
- **Scenarios**:
  - Successful file upload
  - Upload verification
- **Site**: https://the-internet.herokuapp.com/upload

### 6. Dynamic Content Tests (CT-Dynamic-001)
- **Purpose**: Test dynamic content and controls
- **Scenarios**:
  - Content change detection
  - Dynamic control interaction
- **Site**: https://the-internet.herokuapp.com/dynamic_content

<p align="right">(<a href="#top">back to top</a>)</p>

## Usage

Each test suite can be run independently or as part of the complete test suite:

### Running Individual Test Suites
```sh
python ct_login_001/main.py    # Authentication tests
python ct_form_001/main.py     # Form tests
python ct_alert_001/main.py    # Alert tests
python ct_drag_001/main.py     # Drag and drop tests
python ct_upload_001/main.py   # Upload tests
python ct_dynamic_001/main.py  # Dynamic content tests
```

### Test Output
- Detailed console output with test progress
- Clear success/failure indicators
- Step-by-step execution feedback

<p align="right">(<a href="#top">back to top</a>)</p>

## Getting Started

### Prerequisites

* Python 3.6+
* Chrome WebDriver
* pip (Python package installer)
* Git

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/HeitorLouzeiroRepositoryIFPI/trabalho-final-eng-testes.git
   ```

2. Access the project folder
   ```sh
   cd trabalho-final-eng-testes
   ```

3. Create a virtual environment
   ```sh
   python -m venv venv
   ```

4. Activate the virtual environment
   * Windows
   ```sh
   venv\Scripts\activate
   ```
   * Linux/Mac
   ```sh
   source venv/bin/activate
   ```

5. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```

6. Download ChromeDriver
   - Visit: https://sites.google.com/chromium.org/driver/
   - Download the version matching your Chrome browser
   - Add to system PATH or project directory

<p align="right">(<a href="#top">back to top</a>)</p>

## Project Structure

```
trabalho-final-eng-testes/
│
├── ct_login_001/
│   ├── main.py
│   
│
├── ct_form_001/
│   ├── main.py
│   
│
├── ct_alert_001/
│   ├── main.py
│   
│
├── ct_drag_001/
│   ├── main.py
│   
│
├── ct_upload_001/
│   ├── main.py
│  
│
├── ct_dynamic_001/
│   ├── main.py
│  
│
├── requirements.txt
├── LICENSE
└── README.md
```

<p align="right">(<a href="#top">back to top</a>)</p>

## Roadmap

- [x] Implement authentication tests
- [x] Implement form tests
- [x] Implement alert tests
- [x] Implement drag and drop tests
- [x] Implement upload tests
- [x] Implement dynamic content tests


See the [open issues](https://github.com/HeitorLouzeiroRepositoryIFPI/trabalho-final-eng-testes/issues) for a full list of proposed features and known issues.

<p align="right">(<a href="#top">back to top</a>)</p>

## Contributing

Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

## Collaborators

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/42551436?s=400&u=608a3a665aa424e0d6d59b01fa634650979b72ad&v=4" width="100px;" alt="Heitor Louzeiro's Photo"/><br>
        <sub>
          <b>Heitor Louzeiro</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<p align="right">(<a href="#top">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

## Contact

<div align='center'>  
  <a href="https://www.instagram.com/heitorlouzeiro/" target="_blank">
    <img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank">
  </a> 
  <a href = "mailto:heitorlouzeirodev@gmail.com">
    <img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank">    
  </a>
  <a href="https://www.linkedin.com/in/heitor-louzeiro/" target="_blank">
    <img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank">
  </a> 
</div>

<p align="right">(<a href="#top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/HeitorLouzeiroRepositoryIFPI/trabalho-final-eng-testes.svg?style=for-the-badge
[contributors-url]: https://github.com/HeitorLouzeiroRepositoryIFPI/trabalho-final-eng-testes/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/HeitorLouzeiroRepositoryIFPI/trabalho-final-eng-testes.svg?style=for-the-badge
[forks-url]: https://github.com/HeitorLouzeiroRepositoryIFPI/trabalho-final-eng-testes/network/members
[stars-shield]: https://img.shields.io/github/stars/HeitorLouzeiroRepositoryIFPI/trabalho-final-eng-testes.svg?style=for-the-badge
[stars-url]: https://github.com/HeitorLouzeiroRepositoryIFPI/trabalho-final-eng-testes/stargazers
[issues-shield]: https://img.shields.io/github/issues/HeitorLouzeiroRepositoryIFPI/trabalho-final-eng-testes.svg?style=for-the-badge
[issues-url]: https://github.com/HeitorLouzeiroRepositoryIFPI/trabalho-final-eng-testes/issues
[license-shield]: https://img.shields.io/github/license/HeitorLouzeiroRepositoryIFPI/trabalho-final-eng-testes.svg?style=for-the-badge
[license-url]: https://github.com/HeitorLouzeiroRepositoryIFPI/trabalho-final-eng-testes/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/heitor-louzeiro

[Python]: https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[Selenium]: https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white
[Selenium-url]: https://www.selenium.dev/

[unittest]: https://img.shields.io/badge/unittest-047D9C?style=for-the-badge&logo=python&logoColor=white
[unittest-url]: https://docs.python.org/3/library/unittest.html

[Chrome]: https://img.shields.io/badge/Chrome-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white
[Chrome-url]: https://www.google.com/chrome/
