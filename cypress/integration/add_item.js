context('Add Item', () => {
    before(() => {
        cy.visit('/login');
        cy.login();
        cy.visit('/app/item');
    });


    it('adds item', () => {
        cy.get('.primary-action').click();
        //cy.wait(30);
        cy.get('.custom-actions > .btn').click();
        
        cy.get('.layout-main-section > :nth-child(2) > :nth-child(1) > .form-layout > .form-page > :nth-child(1) > .section-body > :nth-child(1) > form > .has-error > .form-group > .control-input-wrapper > .control-input > .input-with-feedback').type('Nokia');
        //cy.get('button.primary-action').contains('Save').click();
        //cy.get(':nth-child(2) > form > .has-error > .form-group > .control-input-wrapper > .control-input > .input-with-feedback').type('70,000');
        //cy.fill_field('price', '70,000');
        //cy.wait(700);
        cy.get(':nth-child(2) > form > [title="price"] > .form-group > .control-input-wrapper > .control-input > .input-with-feedback').wait(1000).type('7000');
        //cy.fill_field('price','7000');
    });


    it('adds item vsbnsn', () => {
        cy.wait(200);
        cy.get('button.primary-action').contains('Save').click();
        //cy.wait(200);
        //cy.get(':nth-child(2) > form > [title="price"] > .form-group > .control-input-wrapper > .control-input > .input-with-feedback').type('70,000');
    });


});
