from unitest import TestCase

from app import app
from models import db, Cupcake

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcake_test'
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True

db.drop_all()
db.create_all()

CUPCAKE_DATA = {
    "flavor": "test",
    "size": "test",
    "rating": 10,
    "image": "test"
}

CUPCAKE_DATA2 = {
    "flavor": "test2",
    "size": "test2",
    "rating": 9,
    "image": "test2"
}

class CupcakeTestCase(TestCase):
    def setUp(self):
        Cupcake.query.delete()
        cupcake = Cupcake(**CUPCAKE_DATA)
        db.session.add_all(cupcake)
        db.session.commit()
        self.cupcake = cupcake
        
        
    def tearDown(self):
        db.session.rollback()
        db.session.remove()
        
    def test_list_cupcake(self):
        with app.test_client() as client:
            resp = client.get('/api/cupcakes')
            data = resp.json
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(data, {'cupcakes': [self.cupcake.serialize()]})
    
    def test_get_cupcake(self):
        with app.test_client() as client:
            resp = client.get(f'/api/cupcakes/{self.cupcake.id}')
            data = resp.json
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(data, {'cupcake': self.cupcake.serialize()})
            
    def test_create_cupcake(self):
        with app.test_client() as client:
            resp = client.post('/api/cupcakes', json=CUPCAKE_DATA2)
            data = resp.json
            self.assertEqual(resp.status_code, 201)
            self.assertEqual(data, {'cupcake': CUPCAKE_DATA2})
            
    def test_delete_cupcake(self):
        with app.test_client() as client:
            resp = client.delete(f'/api/cupcakes/{self.cupcake.id}')
            data = resp.json
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(data, {'message': 'Deleted'})
            
            resp = client.get(f'/api/cupcakes/{self.cupcake.id}')
            self.assertEqual(resp.status_code, 404)
            
            
        
    
            

