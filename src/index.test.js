const sumar = require('./index');
test('Suma correcta ', () => {
  expect(sumar(2, 3)).toBe(5);
});