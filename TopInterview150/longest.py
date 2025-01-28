class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:  # Si la lista está vacía, no hay prefijo común
            return ""

        # Tomamos la primera palabra como referencia inicial
        prefix = strs[0]

        # Recorremos las demás palabras en la lista
        for word in strs[1:]:
            # Comparar el prefijo con cada palabra
            while not word.startswith(prefix):
                # Reducimos el prefijo eliminando el último carácter
                prefix = prefix[:-1]
                # Si el prefijo queda vacío, no hay prefijo común
                if not prefix:
                    return ""
        
        return prefix
