from flask_restful import Resource

class ParticipanteController(Resource):
    # esta clase se comportara como si fuede un controlador, es decir que si definimos un metodo llamado get
    def get(self):
        # SELECT * FROM PARTICIPANTES;
        # https://docs.sqlalchemy.org/en/14/orm/query.html
        # https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query.all
        return{
            'message':'ingreso al get'
        }