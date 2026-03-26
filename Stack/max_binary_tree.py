class Solution:
    def checkValidString(self, s: str) -> bool:
        # cmin: O menor número possível de parênteses abertos
        # cmax: O maior número possível de parênteses abertos
        cmin, cmax = 0, 0

        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin -= 1
                cmax -= 1
            elif char == '*':
                # Pode diminuir o saldo (ser ')'), aumentar (ser '(') ou manter (ser '')
                cmin -= 1
                cmax += 1
            
            # Se cmax for negativo, temos mais ')' do que '(' e '*' juntos.
            # É impossível tornar a string válida.
            if cmax < 0:
                return False
            
            # O cmin não pode ser negativo. Se ele for, significa que usamos
            # um '*' como ')' desnecessariamente; então o tratamos como "" (vazio).
            cmin = max(cmin, 0)

        # Se ao final o mínimo de aberturas necessárias for 0, a string é válida.
        return cmin == 0

# --- Bloco de Teste ---
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = ["()", "(*)", "(*))", "((*)", ")(*"]
    
    print("Resultados dos Testes:")
    for s in test_cases:
        print(f"Input: '{s}' -> Output: {sol.checkValidString(s)}")