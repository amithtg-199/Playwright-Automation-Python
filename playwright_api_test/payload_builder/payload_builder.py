import re
from utils.random_data_generator import RandomDataUtil

PLACEHOLDER_PATTERN = re.compile(r"^\{\{(.+?)\}\}$")

DATA_GENERATORS = {
    "first_name": RandomDataUtil.first_name,
    "last_name": RandomDataUtil.last_name,
    "email": RandomDataUtil.email,
    "phone_number": RandomDataUtil.phone_number,
    "total_price": RandomDataUtil.integer,
    "deposit_paid": RandomDataUtil.boolean,
    "checkin_date": RandomDataUtil.checkin_date,
    "checkout_date": RandomDataUtil.checkout_date,
    "additional_needs": RandomDataUtil.additional_needs,
}


def build_payload(template):
    """
    Builds a dynamic API request payload from a JSON template.

    The function recursively traverses the entire payload, including
    nested dictionaries and lists. When it finds a placeholder such as
    "{{first_name}}", it looks up the corresponding generator from
    DATA_GENERATORS, generates the required value, and replaces the
    placeholder.

    The function also stores all generated values in `generated_data`.
    This allows the same generated test data to be reused later for
    response validation instead of generating new random values.

    Example:
        Template:
            {
                "firstname": "{{first_name}}",
                "lastname": "{{last_name}}"
            }

        Result:
            payload:
                {
                    "firstname": "John",
                    "lastname": "Smith"
                }

            generated_data:
                {
                    "first_name": "John",
                    "last_name": "Smith"
                }

    Returns:
        tuple:
            payload: Fully generated API request payload.
            generated_data: Dictionary containing the values generated
                            while building the payload.

    Note:
        Business-controlled values should normally come from test
        scenarios/configuration rather than being randomly generated.
        The recursive approach allows the same builder to handle both
        simple and very large/nested API payloads.
    """

    generated_data = {}

    def process(value):

        if isinstance(value, dict):

            return {
                key: process(val)
                for key, val in value.items()
            }

        if isinstance(value, list):

            return [
                process(item)
                for item in value
            ]

        if isinstance(value, str):

            match = PLACEHOLDER_PATTERN.match(value)

            if match:

                generator_name = match.group(1)

                generator = DATA_GENERATORS.get(
                    generator_name
                )

                if generator is None:
                    raise ValueError(
                        f"Unknown generator: {generator_name}"
                    )

                generated_value = generator()

                generated_data[generator_name] = generated_value

                return generated_value

        return value

    payload = process(template)

    return payload, generated_data