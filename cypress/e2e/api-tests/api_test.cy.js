describe('API Tests for parfums-esgi.store', () => {
    const apiUrl = 'https://parfums-esgi.store/api';
  
    it('Test GET request', () => {
      cy.request(`${apiUrl}/products`) // Remplacer products
        .its('status')
        .should('eq', 200); // Vérifie que la réponse a un code 200
    });
  
    it('Test POST request', () => {
      cy.request({
        method: 'POST',
        url: `${apiUrl}/products`, // Remplacer products
        body: {
          username: 'testuser',
          password: 'testpassword',
        },
      }).then((response) => {
        expect(response.status).to.eq(200); // Vérifie que la requête est réussie
        expect(response.body).to.have.property('token'); // Vérifie qu'un token est renvoyé
      });
    });
  });
  