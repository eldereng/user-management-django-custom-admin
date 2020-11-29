from utils.format_numerical_text import format_numerical_text


def check_cpf(cpf):
    cpf = format_numerical_text(cpf)
    if len(cpf) < 11:
        return False
    if cpf in [s * 11 for s in [str(n) for n in range(10)]]:
        return False
    d1 = ((sum([int(a) * b
                for a, b in zip(cpf[:-2], list(range(10, 1, -1)))]) * 10) %
          11) % 10
    d2 = (
        (sum([int(a) * b
              for a, b in zip(cpf[:-2], list(range(11, 2, -1)))] + [d1 * 2]) *
         10) % 11) % 10
    return str(d1) == cpf[-2] and str(d2) == cpf[-1]
