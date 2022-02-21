defmodule Luhn do
  @spec suma(String.t()) :: integer()
  def suma(number)do
    #String.split(number,2)
    datos = String.split(number, "", trim: true)
    for dato <- datos do
      valor = String.to_integer(dato)
      numero = valor * 2
    end
  end
end
IO.inspect(Luhn.suma("123456112522"))
