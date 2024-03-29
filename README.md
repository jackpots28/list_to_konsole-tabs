<a name="readme-top"></a>


![GitHub issues](https://img.shields.io/github/issues/jackpots28/list_to_konsole-tabs)
[![GPL License][license-shield]](https://github.com/jackpots28/list_to_konsole-tabs/blob/main/LICENSE)
[![General badge](https://img.shields.io/badge/LinkedIn-Jack_Sims-blue.svg)](https://www.linkedin.com/in/jack-john-sims)




<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Konsole Tabs From File Creator</h3>

  <p align="center">
    Take a newline delimited list and create a "Konsole --tabs-from-file" file
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs » (There are none)</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo (There isn't one)</a>
    ·
    <a href="https://github.com/jackpots28/list_to_konsole-tabs/issues">Report Bug</a>
    ·
    <a href="https://github.com/jackpots28/list_to_konsole-tabs/issues">Request Feature</a>
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
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#Installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With
[![Python][python-badge]](https://www.python.org/)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


## Installation

This is an example of how to list things you need to use the software and how to install them.
* pypi
  ```sh
  pip3 install list-to-tabs
  
  or
  
  python3 -m pip install list-to-tabs
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
```

Run "list-to-tabs" from the cli with option "-h" for Help

or 

Run "list-to-tabs" without any arguments to see narrow usage:

usage: list-to-tabs [-h] [-v] [-b BATCH] [-n NAME] src dest
list-to-tabs: error: the following arguments are required: src, dest

---

Example:

Run against single "server.list" file from "/home/" direcotry and name the output file "batch_file"
.) list-to-tabs /home/your_home/server.list /tmp -n batch_file

Run against multiple "hostfile" lists and output multiple "batch" file subfixed with the original file name
.) ls -lart /path/to/hostfile*.list | awk '{print $9}' | xargs -I{} list-to-tabs ./{} ./ -n batch_{}


```
_For more examples, please refer to the [Documentation]()_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1 - Printing and selecting source files base on a supplied directory
- [ ] Feature 2 - Insertion of different command structures inplace of typical "ssh"

See the [open issues](https://github.com/jackpots28/list_to_konsole-tabs/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Com your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GPL License

[![GPL License][license-shield]](https://github.com/jackpots28/list_to_konsole-tabs/blob/main/LICENSE)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/jackpots28/list_to_konsole-tabs](https://github.com/jackpots28/list_to_konsole-tabs)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
 [![General badge](https://img.shields.io/badge/Github-jackpots28-green.svg)](https://github.com/jackpots28)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/jackpots28/list_to_konsole
[issues-url]: https://github.com/jackpots28/list_to_konsole-tabs/issues
[license-shield]: https://img.shields.io/badge/License-GPLv3-blue.svg
[license-url]: https://github.com/jackpots28/list_to_konsole-tabs/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://linkedin.com/in/linkedin_username
[python-badge]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
