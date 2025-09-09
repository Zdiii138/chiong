import argparse
import qrcode


def generate_qr(data: str, output: str) -> None:
    """Generate a QR code image from the provided data.

    Args:
        data: The text or URL to encode in the QR code.
        output: Path where the generated PNG image will be saved.
    """
    img = qrcode.make(data)
    img.save(output)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a QR code image from text or a URL.")
    parser.add_argument("data", help="Text or URL to encode in the QR code")
    parser.add_argument(
        "-o",
        "--output",
        default="qrcode.png",
        help="Output file name (default: qrcode.png)",
    )
    args = parser.parse_args()

    generate_qr(args.data, args.output)


if __name__ == "__main__":
    main()
