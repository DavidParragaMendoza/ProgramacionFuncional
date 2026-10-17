import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

public class AusenciadeValor {

    public static void main(String[] args) {

        Optional<String> resultado = buscar_producto(3);
        if (resultado.isPresent()) {
            System.out.println(resultado);
            System.out.println(resultado.get().length());
        } else {
            System.out.println("Estado NULL, el producto no existe");
        }

        String re2 = resultado.orElse("VACIO");
        System.out.println(re2);

    }

    public static Optional<String> buscar_producto(int id) {
        Map<Integer, String> listProd = new HashMap<>();
        listProd.put(1, "laptop");
        listProd.put(2, "Mouse");
        return Optional.ofNullable(listProd.get(id));
    }
}