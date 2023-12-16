from flask import Flask, jsonify
from flask.cli import AppGroup

import data.cv_data as cv_data
from error_handler import register_error_handlers
from models.cv_models import (
    EducationInfo,
    Experiences,
    Languages,
    PersonContact,
    TechnicalSkills,
)

app = Flask(__name__)
cli = AppGroup("cv")

register_error_handlers(app)


@app.route("/personal", methods=["GET"])
def get_personal_info():
    """
    Endpoint to retrieve personal information.
    Returns:
        dict: Personal information.
    """
    try:
        personal_info = PersonContact(**cv_data.data["contact"])
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Internal Server Error: {e}"}), 500
    return jsonify(personal_info.model_dump())


@app.route("/skills", methods=["GET"])
def get_skills_info():
    """
    Endpoint to retrieve skills details.
    Returns:
        list: List of languages spoken and technical skills details.
    """
    try:
        languages_info = Languages.model_validate(
            {"languages": cv_data.data["languages"]}
        )
        technical_info = TechnicalSkills.model_validate(
            {"technical_skills": cv_data.data["technical_skills"]}
        )
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Internal Server Error: {e}"}), 500
    return jsonify(languages_info.model_dump(), technical_info.model_dump())


@app.route("/education", methods=["GET"])
def get_education_info():
    """
    Endpoint to retrieve education details.
    Returns:
        list: List of education details.
    """
    try:
        education_info = EducationInfo.model_validate(
            {"education": cv_data.data["education"]}
        )
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Internal Server Error: {e}"}), 500
    return jsonify(education_info.model_dump())


@app.route("/experience", methods=["GET"])
def get_experience_info():
    """
    Endpoint to retrieve experience details.
    Returns:
        list: List of experience details.
    """
    try:
        experience_info = Experiences.model_validate(
            {"experience": cv_data.data["experience"]}
        )
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Internal Server Error: {e}"}), 500
    return jsonify(experience_info.model_dump())


@cli.command("print")
def print_cv_data():
    """
    CLI command to print CV data to the console.
    """
    try:
        print("\nPersonal Information:")
        for k, v in cv_data.data["contact"].items():
            if isinstance(v, dict):
                for lk, lv in v.items():
                    print(f"{lk}: {lv}")
                continue
            print(f"{k}: {v}")

        print("\nExperience:")
        for exp in cv_data.data["experience"]:
            for k, v in exp.items():
                if isinstance(v, list):
                    for contribution in v:
                        print(f"\u2022 {contribution}")
                    continue
                print(f"{k}: {v}")
            print("\n")

        print("\nEducation:")
        for edu in cv_data.data["education"]:
            for k, v in edu.items():
                print(f"{k}: {v}")

        print("\nTechnical skills:")
        for skill in cv_data.data["technical_skills"]:
            print(f"{skill['name']}: {', '.join(skill['keywords'])}")
    except Exception as e:
        print(f"Error: {e}")


app.cli.add_command(cli)


if __name__ == "__main__":
    app.run(debug=True)
