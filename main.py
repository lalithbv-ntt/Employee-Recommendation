from flask import Flask, render_template, request
import recommender

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        result = request.form
        result = result.to_dict()
        requirement = {"REQUIREMENT": {
            "Basic Data Manipulation": int(result.get('Basic Data Manipulation') or 1),
            "Advanced ETL": int(result.get('Advanced ETL') or 1),
            "Data Architecture": int(result.get('Data Architecture') or 1),
            "Data Modelling and Design": int(result.get('Data Modelling and Design') or 1),
            "Data Storage and Operations": int(result.get('Data Storage and Operations') or 1),
            "Data Security": int(result.get('Data Security') or 1),
            "Reference and Master Data Management": int(result.get('Reference and Master Data Management') or 1),
            "Document and Content Management": int(result.get('Document and Content Management') or 1),
            "Data Governance": int(result.get('Data Governance') or 1),
            "Data Quality Management": int(result.get('Data Quality Management') or 1),
            "Metadata Management": int(result.get('Metadata Management') or 1),
            "Developing a Data Strategy": int(result.get('Developing a Data Strategy') or 1),
            "Exploratory Analysis": int(result.get('Exploratory Analysis') or 1),
            "Statistical Testing": int(result.get('Statistical Testing') or 1),
            "Data Visualisation": int(result.get('Data Visualisation') or 1),
            "Report Design and Development": int(result.get('Report Design and Development') or 1),
            "Predictive Analytics": int(result.get('Predictive Analytics') or 1),
            "Unsupervised Learning": int(result.get('Unsupervised Learning') or 1),
            "Forecasting": int(result.get('Forecasting') or 1),
            "Developing an Analytics Strategy": int(result.get('Developing an Analytics Strategy') or 1),
            "SQL Server": int(result.get('SQL Server') or 1),
            "Oracle": int(result.get('Oracle') or 1),
            "MySQL": int(result.get('MySQL') or 1),
            "Postgres": int(result.get('Postgres') or 1),
            "Marklogic": int(result.get('Marklogic') or 1),
            "CosmosDB": int(result.get('CosmosDB') or 1),
            "SQL Data Warehouse": int(result.get('SQL Data Warehouse') or 1),
            "Redshift": int(result.get('Redshift') or 1),
            "Snowflake": int(result.get('Snowflake') or 1),
            "Azure": int(result.get('Azure') or 1),
            "AWS": int(result.get('AWS') or 1),
            "Google Cloud Platform": int(result.get('Google Cloud Platform') or 1),
            "T-SQL": int(result.get('T-SQL') or 1),
            "PL/SQL": int(result.get('PL/SQL') or 1),
            "R": int(result.get('R') or 1),
            "Python": int(result.get('Python') or 1),
            "Java": int(result.get('Java') or 1),
            "XQuery": int(result.get('XQuery') or 1),
            "SPARQL": int(result.get('SPARQL') or 1),
            ".NET": int(result.get('.NET') or 1),
            "CSS/HTML": int(result.get('CSS/HTML') or 1),
            "Power BI": int(result.get('Power BI') or 1),
            "Tableau": int(result.get('Tableau') or 1),
            "Qlikview": int(result.get('Qlikview') or 1),
            "SSIS": int(result.get('SSIS') or 1),
            "SSRS": int(result.get('SSRS') or 1),
            "SSAS": int(result.get('SSAS') or 1),
            "Azure Data Factory": int(result.get('Azure Data Factory') or 1),
            "Azure Databricks": int(result.get('Azure Databricks') or 1),
            "Alteryx": int(result.get('Alteryx') or 1),
            "Apache Nifi": int(result.get('Apache Nifi') or 1),
            "Business Objects Data Services": int(result.get('Business Objects Data Services') or 1),
            "Banking and Finance": int(result.get('Banking and Finance') or 1),
            "Energy and Resources": int(result.get('Energy and Resources') or 1),
            "Utilities": int(result.get('Utilities') or 1),
            "Education": int(result.get('Education') or 1),
            "Health": int(result.get('Health') or 1),
            "Defence": int(result.get('Defence') or 1),
            "Other Government": int(result.get('Other Government') or 1),
            "Project Management": int(result.get('Project Management') or 1),
            "Waterfall": int(result.get('Waterfall') or 1),
            "Presentation Skills": int(result.get('Presentation Skills') or 1),
            "C-Level Communication/Meetings": int(result.get('C-Level Communication/Meetings') or 1),
            "Team Management": int(result.get('Team Management') or 1),
            "Stakeholder Management": int(result.get('Stakeholder Management') or 1)}}
        num_of_candidate = int(result.get('candidate') or 5)
        result = recommender.topMatches(requirement, recommender.dataFrame, "REQUIREMENT", num_of_candidate)
        print("******************************")
        print(result)
        print("******************************")
        return render_template("index.html", result=result)

    return render_template("index.html", result=[("Name","Score")])


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0)
