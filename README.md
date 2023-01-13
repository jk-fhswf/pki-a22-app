# Haar Cascade Evaluation Apps with Streamlit and Tkinter


In this project we developed an object detection App using Haar Cascade classifier in two different ways: one as web dashboard with [Streamlit](https://streamlit.io/) and one as desktop app using Tkinter. 

Here is a [demo](https://jk-fhswf-pki-a22-app-app-codcuk.streamlit.app/) of the Streamlit app deployed on the Streamlit cloud platform.

### TODO: (Screenshot of apps)

### Installing

We generally recommend installing the library inside a virtual environment

```
pip install git+https://github.com/jk-fhswf/pki-a22-app.git
```

### Executing program

The Streamlit app can be executed using the streamlit module: 
```
stremlit run app.py
```

For starting the Tkinter app use:

```
python app_tkinter.py
```

# Development

## Prerequisites

We use [poetry](https://python-poetry.org/) as package manager. Please make sure to have poetry installed before.

## Dependencies

To setup a virtual environment with all necessary dependencies use the poetry package manager:

```
poetry install
```

This will create a virtual environment inside the folder ".venv". 

### Development Environment

All common development environments for python support the poetry package manager by default. We used Pycharm and VSCode.

## Export requirements file

If you want to use a different virtual environment you can export the dependencies using:
```
poetry export -f requirements.txt --output requirements.txt
```


## Implementation with Streamlit

![Streamlit Landing Page](doc/images/streamlit/2023-01-11-16-22-07.png)

## Live Demo

The project is deployed on the Streamlit cloud:

https://jk-fhswf-pki-a22-app-app-codcuk.streamlit.app/


## Authors

The project was developed by the following persons.

TODO: email-addressen

Tkinter:
* Alexander Fuchs
* Onur Yilmaz
* Peter Spanke

Streamlit:
* Johannes-Peter Kübert

Documentation
* Onur Yilmaz

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)

## References

TODO

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)

