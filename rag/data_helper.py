try:
    import pdftotext
except ImportError:
    pdftotext = None


class PDFReader:
    def _init_(self, pdf_paths: list[str] | str):
        if isinstance(pdf_paths, str):
            pdf_paths = [pdf_paths]
        self.pdf_path = pdf_paths

    def read(self) -> list[str]:
        if pdftotext is None:
            raise ImportError("pdftotext is required for PDFReader. Install it with: pip install pdftotext")
        texts = []
        for pdf_path in self.pdf_path:
            with open(pdf_path, "rb") as file:
                pdf = pdftotext.PDF(file)
                # Join all pages into a single string by \n\n
                texts.append("\n\n".join(pdf))
        return texts
