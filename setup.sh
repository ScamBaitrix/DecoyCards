#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${GREEN}"
echo "  ===================================="
echo "   DecoyCards - Easy Setup by Baitrix"
echo "  ===================================="
echo -e "${NC}"
echo "  This will install everything you need!"
echo ""
echo -e "${YELLOW}  WARNING: This makes FAKE gift card codes"
echo "  for scambaiting only!"
echo -e "${NC}"
echo ""
read -p "Press Enter to continue..."

echo ""
echo -e "[1/4] Checking if Python is installed..."

if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    echo -e "${GREEN}Python 3 found: $(python3 --version)${NC}"
elif command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version 2>&1)
    if [[ $PYTHON_VERSION == *"Python 3"* ]]; then
        PYTHON_CMD="python"
        echo -e "${GREEN}Python 3 found: $PYTHON_VERSION${NC}"
    else
        echo -e "${RED}Python 3 required but found: $PYTHON_VERSION${NC}"
        echo "Please install Python 3.7+ from: https://www.python.org/downloads/"
        exit 1
    fi
else
    echo -e "${RED}Python not found!${NC}"
    echo "Please install Python 3.7+ from: https://www.python.org/downloads/"
    exit 1
fi

echo ""
echo "[2/4] Upgrading pip..."
$PYTHON_CMD -m pip install --upgrade pip

echo ""
echo "[3/4] Installing required packages..."
$PYTHON_CMD -m pip install customtkinter requests playsound

echo ""
echo "[4/4] Creating launcher scripts..."
cat > start_gui.sh << EOF
#!/bin/bash
cd "\$(dirname "\$0")"
if command -v python3 &> /dev/null; then
    python3 gift_card_generator.py --gui
elif command -v python &> /dev/null; then
    python gift_card_generator.py --gui
else
    echo "Python not found! Please run setup.sh first."
    read -p "Press Enter to exit..."
fi
EOF

cat > start_cli.sh << EOF
#!/bin/bash
cd "\$(dirname "\$0")"
if command -v python3 &> /dev/null; then
    python3 gift_card_generator.py
elif command -v python &> /dev/null; then
    python gift_card_generator.py
else
    echo "Python not found! Please run setup.sh first."
    read -p "Press Enter to exit..."
fi
EOF

chmod +x start_gui.sh
chmod +x start_cli.sh

echo ""
echo -e "${GREEN}"
echo "  ===================================="
echo "   Setup Complete!"
echo "  ===================================="
echo -e "${NC}"
echo "  DecoyCards is ready to use!"
echo ""
echo "  TO START:"
echo "  - Run: ./start_gui.sh for easy interface"
echo "  - Run: ./start_cli.sh for menu version"
echo ""
echo -e "${YELLOW}  REMEMBER: These are FAKE codes for scambaiting only!"
echo -e "${NC}"
echo ""
read -p "Press Enter to exit..."
